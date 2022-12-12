from typing import Any, Callable, List
from bilibili import *
import xbmcgui
import xbmc
import json
import os
import xbmcaddon


class Common:
    @staticmethod
    def selectVideo(videos: List[WebSearchVideo], title="Search Result", prevPage: str = None, nextPage: str = None, initSelect=None, onSelect: Callable[[int], None] = None):  # type: ignore
        def markup(txt: str) -> str:
            return txt.replace('<em class="keyword">', '[COLOR red]').replace('</em>', '[/COLOR]').replace('&amp;', '&')

        selections: List[str] = []
        selections.extend([prevPage])
        selections.extend(["({}){}".format(x['author'], markup(x['title'])) if 'author' in x else markup(x['title']) for x in videos])
        selections.extend([nextPage])
        selections = [x for x in selections if x is not None]

        index = xbmcgui.Dialog().select(title, selections, preselect=initSelect if initSelect is not None else -1)  # type:ignore

        if index < 0:
            return "fin"

        if selections[index] == prevPage:
            return 'prevPage'
        elif selections[index] == nextPage:
            return 'nextPage'

        if onSelect is not None:
            onSelect(index)

        progress = xbmcgui.DialogProgress()
        progress.create('', 'loading video')

        video = videos[index]

        # debug
        #  xbmcgui.Dialog().textviewer('', '\n'.join(['{}: {}'.format(k, v) for k, v in video.items()]), usemono=True)

        videoDetail = Api.videoDetail(video)

        if not videoDetail:
            raise Exception('no resp detail')

        url = Api.videoHtml5Url(videoDetail)

        if not url:
            raise Exception('no resp playurl')

        progress.close()

        RecentHistory.addHistoryEntry(video)
        playVideo(url)

        return "again"

    @staticmethod
    def videoSelectionListPaged(getVideos: Callable[[int], List[WebSearchVideo]], title="Search Result", initPage=1):
        curPage = initPage
        needsUpdate = True
        preselect = None

        i = 0
        videos = None

        def resetPreselect(index: int):
            nonlocal preselect
            preselect = index

        while True:
            if needsUpdate:
                videos = getVideos(curPage)
                needsUpdate = False

            if videos is None:
                raise Exception('getVideos failed')

            ret = Common.selectVideo(videos, title=title,
                                     prevPage=None if curPage == 1 else '<< Last Page',  # type:ignore
                                     nextPage=None if curPage >= 10 or len(videos) == 0 else '>> Next Page',  # type:ignore
                                     initSelect=preselect, onSelect=resetPreselect)

            if ret == 'prevPage':
                curPage -= 1
                needsUpdate = True
                preselect = None
            elif ret == 'nextPage':
                curPage += 1
                needsUpdate = True
                preselect = None

            i += 1

            if ret == 'fin':
                break

        return 'fin'

    # new selections
    @staticmethod
    def selectList(selections: List[str], title, prevPage=False, nextPage=False, preselect=-1):
        sels = []

        prevPageTxt = '<< Last Page...'
        nextPageTxt = '>> Next Page...'

        if prevPage:
            sels.extend([prevPageTxt])

        sels.extend(selections)

        if nextPage:
            sels.extend([nextPageTxt])

        index = xbmcgui.Dialog().select(title, sels, preselect=preselect)

        if index < 0:
            return ("fin", None)
        if sels[index] == prevPageTxt:
            return ('prevPage', None)
        elif sels[index] == nextPageTxt:
            return ('nextPage', None)

        return ('select', index)

    @staticmethod
    def selectListPaged(getSelections: Callable[[int], List[Any]], getEntryTxt: Callable[[Any], str], title: str, initPage=1):
        curPage = initPage
        needsUpdate = True
        preselect = -1

        i = 0
        selections: List[Any] = None  # type:ignore
        selectionLabels: List[str] = None  # type:ignore

        while True:
            if needsUpdate:
                selections = getSelections(curPage)
                selectionLabels = [getEntryTxt(x) for x in selections]
                needsUpdate = False

            if selections is None:
                raise Exception('getVideos failed')

            ret, arg = Common.selectList(selectionLabels, title=title,
                                         prevPage=curPage > 1,
                                         nextPage=curPage < 10,
                                         preselect=preselect)
            if ret == 'select':
                return ("select", selections[cast(int, arg)])

            if ret == 'prevPage' or ret == 'nextPage':
                if ret == 'prevPage':
                    curPage -= 1
                else:
                    curPage += 1
                preselect = -1
                needsUpdate = True

            i += 1

            if ret == 'fin':
                break

        return ('fin', None)


class DefaultSearch:
    @staticmethod
    def start():
        query = xbmcgui.Dialog().input('Default Search').strip()

        if len(query) == 0:
            return "fin"

        def updateVideos(page=1):
            progress = xbmcgui.DialogProgress()
            progress.create('searching: ' + query)

            videos = Api.webSearchVideos(query, page)

            progress.close()

            return videos

        return Common.videoSelectionListPaged(cast(Callable[[int], List[WebSearchVideo]], updateVideos))  # force cast


class RecentHistory:
    _history: List[WebSearchVideo] = None  # type: ignore

    @staticmethod
    def filePath():
        profile = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile'))  # .decode("utf-8")
        return os.path.join(profile, 'history.json')

    @staticmethod
    def writeFile():
        if RecentHistory._history is None:
            return

        path = RecentHistory.filePath()
        dir = os.path.dirname(path)
        if not os.path.isdir(dir):
            os.mkdir(dir)
        f = open(path, "w")
        json.dump([{k: v for k, v in x.items() if k in list(WebSearchVideo.__annotations__.keys())} for x in RecentHistory._history], f)
        f.close()

    @staticmethod
    def addHistoryEntry(video: WebSearchVideo):
        if RecentHistory._history is None:
            RecentHistory._history = RecentHistory.getHistory()

        history = RecentHistory._history
        for v in history:
            if v['bvid'] == video['bvid']:
                history.remove(v)
                break
        history.insert(0, video)

        MAX_LEN = 20
        if len(history) > MAX_LEN:
            history.pop()

    @staticmethod
    def getHistory() -> List[WebSearchVideo]:
        if RecentHistory._history is None:
            path = RecentHistory.filePath()
            if os.path.exists(path):
                f = open(path, "r")
                RecentHistory._history = json.load(f)
                f.close()
            else:
                RecentHistory._history = []

        return RecentHistory._history

    @staticmethod
    def start():
        historyVideos = RecentHistory.getHistory()

        i = 0
        while True:
            if len(historyVideos) == 0:
                xbmcgui.Dialog().ok('', 'Empty History')
                return 'fin'

            ret = Common.selectVideo(historyVideos, title="History")
            i += 1
            if ret == 'fin':
                return ret


class SearchUser:
    @staticmethod
    def start():
        query = xbmcgui.Dialog().input('Search User').strip()

        if len(query) == 0:
            return "fin"

        def getUsers(page: int):
            res = Api.webSearchUsers(query, page)
            if not res:
                raise UserException('web search users failed')
            return res

        def getUserLabel(user: WebSearchUser):
            uname = user['uname'].replace('\n', '\\n')
            usign = user['usign'].replace('\n', '\\n').strip()
            if len(usign) > 0:
                return "{} ({})".format(uname, usign)
            return uname

        ret, user = Common.selectListPaged(getUsers, getUserLabel, 'Search Result')
        if ret == 'fin':
            return 'again'
        elif ret == 'select':
            user = cast(WebSearchUser, user)
            ret = Common.videoSelectionListPaged(lambda page: Api.getUserVideos(user, page), "Videos from {}".format(getUserLabel(user)))

        return 'fin'


def playVideo(path):
    player = xbmc.Player()

    HEADER = 'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36' \
        + '&Referer=https://www.bilibili.com' \
        + '&Range=bytes=0-' \
        + '&Connection=keep-alive'\
        + '&Origin=https://www.bilibili.com' \
        + '&Accept-Encoding=gzip, deflate, br'

    player.play(path + '|' + HEADER)

    #  player.play(path)

    while not player.isPlaying():
        xbmc.sleep(200)
        pass

    xbmc.log('start playing', xbmc.LOGINFO)

    # block until video is stopped
    while player.isPlaying():
        xbmc.sleep(200)
        pass

    xbmc.sleep(10)

    xbmc.log('finish playing', xbmc.LOGINFO)
