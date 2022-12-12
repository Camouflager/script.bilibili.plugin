from typing import List, TypedDict, cast, Optional
import uuid
import os
import xbmc
import xbmcaddon
import json
import requests
from api import API


class UserException(Exception):
    pass


class WebSearchVideo(TypedDict):
    title: str
    bvid: str
    aid: str
    author: str


class VideoDetail(dict):
    pass


class WebSearchUser(TypedDict):
    mid: int
    uname: str
    usign: str  # autograph


class Api:
    @staticmethod
    def getUserVideos(user: WebSearchUser, page: int, keyword=""):
        #  ps      (int, optional)       : 每一页的视频数. Defaults to 30.
        #  tid     (int, optional)       : 分区 ID. Defaults to 0（全部）.
        ps = 30
        tid = 0
        params = {
            "mid": user['mid'],
            "ps": ps,
            "tid": tid,
            "pn": page,
            "keyword": keyword,
            "order": "pubdate",
        }

        def parse(resp: dict):
            return resp['list']['vlist']  # vlist

        resp = request("GET", API['user']['info']['video']['url'], params=params)
        if resp is None:
            raise UserException('get user video failed')
        return parse(resp)

    @staticmethod
    def webSearchUsers(keyword: str, page: int):
        def parse(resp: dict) -> List[WebSearchUser]:
            if 'result' in resp:
                return resp['result']
            raise UserException('No more results')

        params = {
            "keyword": keyword,
            "page": page,
            "search_type": "bili_user",
        }
        resp = request("GET", API['search']['web_search_by_type']['url'], params=params)
        return parse(resp) if resp else None

    @staticmethod
    def webSearchVideos(keyword: str, page: int):
        def parseWebSearchResults(resp: dict) -> List[WebSearchVideo]:
            videos = [x for x in resp['result'] if x['result_type'] == 'video'][0]['data']
            videos = [cast(WebSearchVideo, x) for x in videos]
            return videos
        resp = request("GET", API['search']['web_search']['url'], params={"keyword": keyword, "page": page})
        return parseWebSearchResults(resp) if resp else None

    @staticmethod
    def videoDetail(video: WebSearchVideo):
        detailUrl = API["video"]["info"]["detail"]["url"]
        bvid = video['bvid']
        aid = video["aid"]
        params = {"bvid": bvid, "aid": aid}
        return cast(VideoDetail, request("GET", detailUrl, params=params))

    @staticmethod
    def videoHtml5Url(videoDetail: VideoDetail):
        aid = videoDetail['aid']
        cid = videoDetail['pages'][0]['cid']

        # get download url
        playurl = API['video']['info']['playurl']['url']
        params = {
            "avid": aid,
            "cid": cid,
            "qn": 80,
            "otype": "json",
            "fnval": 0,
            "fourk": 0,
            #  "platform": "html5",
        }

        resp = request('GET', playurl, params, tryGetCredentials())

        if resp:
            #  import xbmcgui
            #  xbmcgui.Dialog().textviewer('', str(resp))
            return cast(str, resp['durl'][0]['url'])


class Credentials(TypedDict):
    BILI_JCT: str
    BUVID3: str
    SESSDATA: str


def tryGetCredentials() -> Optional[Credentials]:
    profile = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile'))  # .decode("utf-8")
    path = os.path.join(profile, 'credentials.json')
    if os.path.exists(path):
        f = open(path, 'r')
        return json.load(f)
    return None


def request(method: str, url: str, params: dict, credentials: Optional[Credentials] = None):
    method = method.upper()

    # 使用 Referer 和 UA 请求头以绕过反爬虫机制
    DEFAULT_HEADERS = {
        "Referer": "https://www.bilibili.com",
        "User-Agent": "Mozilla/5.0",
    }
    headers = DEFAULT_HEADERS

    if params is None:
        params = {}

    cookies = {
        "SESSDATA": credentials.get('SESSDATA', None) if credentials else None,
        "buvid3": str(uuid.uuid1()) + "infoc" if not credentials else credentials["BUVID3"],
        "bili_jct": credentials.get('BILI_JCT', None) if credentials else None,
        "DedeUserID": None,
    }
    cookies["buvid3"] = str(uuid.uuid1())
    cookies["Domain"] = ".bilibili.com"

    config = {
        "method": method,
        "url": url,
        "params": params,
        "data": None,
        "headers": headers,
        "cookies": cookies,
    }

    #  if json_body:
    #      config["headers"]["Content-Type"] = "application/json"
    #      config["data"] = json.dumps(config["data"])

    # config["ssl"] = False

    # config["verify_ssl"] = False
    # config["ssl"] = False

    #  session = get_session()

    resp = requests.request(**config)

    # 检查响应头 Content-Length
    content_length = resp.headers.get("content-length")
    if content_length and int(content_length) == 0:
        return None

    # 检查响应头 Content-Type
    content_type = resp.headers.get("content-type")

    # 不是 application/json
    if content_type and content_type.lower().index("application/json") == -1:
        raise UserException("响应不是 application/json 类型")

    raw_data = resp.text
    resp_data: dict

    resp_data = json.loads(raw_data)

    # 检查 code
    code = resp_data.get("code", None)

    if code is None:
        raise UserException(-1, "API 返回数据未含 code 字段", resp_data)
    if code != 0:
        msg = resp_data.get("msg", None)
        if msg is None:
            msg = resp_data.get("message", None)
        if msg is None:
            msg = "接口未返回错误信息"
        raise UserException(code, msg, resp_data)

    real_data = resp_data.get("data", None)
    if real_data is None:
        real_data = resp_data.get("result", None)

    return real_data
