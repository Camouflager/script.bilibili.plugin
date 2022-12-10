# Adapted from https://github.com/Nemo2011/bilibili-api

# So json can be copied directly
true = True
false = False

API = {
    "search": {
        "web_search": {
            "url": "https://api.bilibili.com/x/web-interface/search/all/v2",
            "method": "GET",
            "verify": false,
            "params": {
                "keyword": "str: 搜索用的关键字",
                "page": "int: 页码"
            },
            "comment": "在首页以关键字搜索，只指定关键字，其他参数不指定"
        },
        "web_search_by_type": {
            "url": "https://api.bilibili.com/x/web-interface/search/type",
            "method": "GET",
            "verify": false,
            "params": {
                "keyword": "str: 搜索用的关键字",
                "search_type": "str: 搜索时限定类型：视频(video)、番剧(media_bangumi)、影视(media_ft)、直播(live)、专栏(article)、话题(topic)、用户(bili_user)",
                "page": "int: 页码"
            },
            "comment": "搜索关键字时限定类型,可以指定排序号"
        },
        "default_search_keyword": {
            "url": "https://api.bilibili.com/x/web-interface/search/default",
            "method": "GET",
            "verify": false,
            "comment": "获取默认的搜索内容"
        },
        "hot_search_keywords": {
            "url": "https://s.search.bilibili.com/main/hotword",
            "method": "GET",
            "verify": false,
            "comment": "获取热搜"
        },
        "suggest": {
            "url": "https://s.search.bilibili.com/main/suggest",
            "method": "GET",
            "verify": false,
            "comment": "获取搜索建议"
        },
        "game": {
            "url": "https://line1-h5-pc-api.biligame.com/game/wiki/search",
            "method": "GET",
            "params": {
                "keyword": "str: 搜索用的关键字"
            },
            "verify": false,
            "comment": "搜索游戏"
        }
    },
    "video": {
        "info": {
            "stat": {
                "url": "https://api.bilibili.com/x/web-interface/archive/stat",
                "method": "GET",
                "verify": false,
                "params": {
                    "aid": "int: av 号",
                    "bvid": "string: BV 号"
                },
                "comment": "视频数据"
            },
            "detail": {
                "url": "https://api.bilibili.com/x/web-interface/view",
                "method": "GET",
                "verify": false,
                "params": {
                    "aid": "int: av 号",
                    "bvid": "string: BV 号"
                },
                "comment": "视频详细信息"
            },
            "tags": {
                "url": "https://api.bilibili.com/x/tag/archive/tags",
                "method": "GET",
                "verify": true,
                "params": {
                    "aid": "int: av 号",
                    "bvid": "string: BV 号"
                },
                "comment": "视频标签信息"
            },
            "chargers": {
                "url": "https://api.bilibili.com/x/web-interface/elec/show",
                "method": "GET",
                "verify": false,
                "params": {
                    "aid": "int: av 号",
                    "bvid": "string: BV 号",
                    "mid": "int: 用户 UID"
                },
                "comment": "视频充电信息"
            },
            "video_snapshot_pvideo": {
                "url": "https://api.bilibili.com/pvideo",
                "method": "GET",
                "verify": false,
                "params": {
                    "aid": "int: av 号"
                },
                "comment": "视频预览快照(web)"
            },
            "video_snapshot": {
                "url": "https://api.bilibili.com/x/player/videoshot",
                "method": "GET",
                "verify": false,
                "params": {
                    "aid": "int: av 号",
                    "bvid": "string: BV 号",
                    "cid": "int:分 P CID",
                    "index": "int:json 数组截取时间表1为需要，0不需要"
                },
                "comment": "视频快照(web)"
            },
            "pages": {
                "url": "https://api.bilibili.com/x/player/pagelist",
                "method": "GET",
                "verify": false,
                "params": {
                    "aid": "int: av 号",
                    "bvid": "string: BV 号"
                },
                "comment": "分 P 列表"
            },
            "playurl": {
                "url": "https://api.bilibili.com/x/player/playurl",
                "method": "GET",
                "verify": false,
                "params": {
                    "avid": "int: av 号",
                    "cid": "int: 分 P 编号",
                    "qn": "int: 视频质量编号，最高 127",
                    "otype": "const str: json",
                    "fnval": "const int: 4048",
                    "platform": "int: 平台"
                },
                "comment": "视频下载的信息，下载链接需要提供 headers 伪装浏览器请求（Referer 和 User-Agent）"
            },
            "related": {
                "url": "https://api.bilibili.com/x/web-interface/archive/related",
                "method": "GET",
                "verify": false,
                "params": {
                    "aid": "int: av 号",
                    "bvid": "string: BV 号"
                },
                "comment": "获取关联视频"
            },
            "has_liked": {
                "url": "https://api.bilibili.com/x/web-interface/archive/has/like",
                "method": "GET",
                "verify": true,
                "params": {
                    "aid": "int: av 号",
                    "bvid": "string: BV 号"
                },
                "comment": "是否已点赞"
            },
            "get_pay_coins": {
                "url": "https://api.bilibili.com/x/web-interface/archive/coins",
                "method": "GET",
                "verify": true,
                "params": {
                    "aid": "int: av 号",
                    "bvid": "string: BV 号"
                },
                "comment": "是否已投币"
            },
            "has_favoured": {
                "url": "https://api.bilibili.com/x/v2/fav/video/favoured",
                "method": "GET",
                "verify": true,
                "params": {
                    "aid": "int: av 号"
                },
                "comment": "是否已收藏"
            },
            "media_list": {
                "url": "https://api.bilibili.com/x/v3/fav/folder/created/list-all",
                "method": "GET",
                "verify": true,
                "params": {
                    "rid": "int: av 号",
                    "up_mid": "int: up 主的 uid",
                    "type": "const int: 2"
                },
                "comment": "获取收藏夹列表信息，用于收藏操作"
            },
            "get_player_info": {
                "url": "https://api.bilibili.com/x/player/v2",
                "method": "GET",
                "verify": true,
                "data": {
                    "aid": "int: av 号。与 bvid 任选其一",
                    "cid": "int: 分 P id",
                    "bvid": "int: bv 号。与 aid 任选其一"
                },
                "comment": "获取视频上一次播放的记录，字幕和地区信息。需要 分集的 cid, 返回数据中含有json字幕的链接"
            },
            "pbp": {
                "url": "https://bvc.bilivideo.com/pbp/data",
                "method": "GET",
                "verify": false,
                "params": {
                    "cid": "int: 分 P 编号",
                    "bvid": "string: BV 号",
                    "aid": "int: av 号"
                }
            }
        },
        "operate": {
            "like": {
                "url": "https://api.bilibili.com/x/web-interface/archive/like",
                "method": "POST",
                "verify": true,
                "data": {
                    "aid": "int: av 号",
                    "bvid": "string: BV 号",
                    "like": "int: 1 是点赞，2 是取消点赞"
                },
                "comment": "给视频点赞/取消点赞 "
            },
            "coin": {
                "url": "https://api.bilibili.com/x/web-interface/coin/add",
                "method": "POST",
                "verify": true,
                "data": {
                    "aid": "int: av 号",
                    "bvid": "string: BV 号",
                    "multiply": "int: 几个币",
                    "select_like": "int bool: 是否同时点赞"
                },
                "comment": "给视频投币"
            },
            "add_tag": {
                "url": "https://api.bilibili.com/x/tag/archive/add",
                "method": "POST",
                "verify": true,
                "data": {
                    "aid": "int: av 号",
                    "tag_name": "str: 标签名"
                },
                "comment": "添加标签"
            },
            "del_tag": {
                "url": "https://api.bilibili.com/x/tag/archive/del",
                "method": "POST",
                "verify": true,
                "data": {
                    "aid": "int: av 号",
                    "tag_id": "int: 标签 id"
                },
                "comment": "删除标签"
            },
            "subscribe_tag": {
                "url": "https://api.bilibili.com/x/tag/subscribe/add",
                "method": "POST",
                "verify": true,
                "data": {
                    "tag_id": "int: 标签 id"
                },
                "comment": "订阅标签"
            },
            "unsubscribe_tag": {
                "url": "https://api.bilibili.com/x/tag/subscribe/cancel",
                "method": "POST",
                "verify": true,
                "data": {
                    "tag_id": "int: 标签 id"
                },
                "comment": "取消订阅标签"
            },
            "favorite": {
                "url": "https://api.bilibili.com/x/v3/fav/resource/deal",
                "method": "POST",
                "verify": true,
                "data": {
                    "rid": "int: av 号。",
                    "type": "const int: 2",
                    "add_media_ids": "commaSeparatedList[int]: 要添加到的收藏夹 ID。",
                    "del_media_ids": "commaSeparatedList[int]: 要移出的收藏夹 ID。"
                },
                "comment": "设置视频收藏状态"
            },
            "submit_subtitle": {
                "url": "https://api.bilibili.com/x/v2/dm/subtitle/draft/save",
                "method": "POST",
                "verify": true,
                "data": {
                    "type": 1,
                    "oid": "int: 分 P id",
                    "lan": "str: 字幕语言代码，参考 http://www.lingoes.cn/zh/translator/langcode.htm",
                    "data": {
                        "font_size": "float: 字体大小，默认 0.4",
                        "font_color": "str: 字体颜色，默认 \"#FFFFFF\"",
                        "background_alpha": "float: 背景不透明度，默认 0.5",
                        "background_color": "str: 背景颜色，默认 \"#9C27B0\"",
                        "Stroke": "str: 描边，目前作用未知，默认为 \"none\"",
                        "body": [
                            {
                                "from": "int: 字幕开始时间（秒）",
                                "to": "int: 字幕结束时间（秒）",
                                "location": "int: 字幕位置，默认为 2",
                                "content": "str: 字幕内容"
                            }
                        ]
                    },
                    "submit": "bool: 是否提交，不提交为草稿",
                    "sign": "bool: 是否署名",
                    "bvid": "str: 视频 BV 号"
                },
                "comment": "上传字幕"
            }
        },
        "danmaku": {
            "get_danmaku": {
                "url": "https://api.bilibili.com/x/v2/dm/web/seg.so",
                "method": "GET",
                "verify": false,
                "params": {
                    "oid": "int: video_info 中的 cid，即分 P 的编号",
                    "type": "const int: 1",
                    "segment_index": "int: 分片序号",
                    "pid": "int: av 号"
                },
                "comment": "获取弹幕列表"
            },
            "get_history_danmaku": {
                "url": "https://api.bilibili.com/x/v2/dm/web/history/seg.so",
                "method": "GET",
                "verify": true,
                "params": {
                    "oid": "int: video_info 中的 cid，即分 P 的编号",
                    "type": "const int: 1",
                    "date": "str: 历史弹幕日期，格式：YYYY-MM-DD"
                },
                "comment": "获取历史弹幕列表"
            },
            "view": {
                "url": "https://api.bilibili.com/x/v2/dm/web/view",
                "method": "GET",
                "verify": false,
                "params": {
                    "type": 1,
                    "oid": "int: 分 P 的编号",
                    "pid": "int: av 号"
                },
                "comment": "获取弹幕设置、特殊弹幕"
            },
            "get_history_danmaku_index": {
                "url": "https://api.bilibili.com/x/v2/dm/history/index",
                "method": "GET",
                "verify": true,
                "params": {
                    "oid": "int: 分 P 的编号",
                    "type": "const int: 1",
                    "month": "str: 年月 (yyyy-mm)"
                },
                "comment": "存在历史弹幕的日期"
            },
            "has_liked_danmaku": {
                "url": "https://api.bilibili.com/x/v2/dm/thumbup/stats",
                "method": "GET",
                "verify": true,
                "params": {
                    "oid": "int: video_info 中的 cid，即分 P 的编号",
                    "ids": "commaSeparatedList[int]: 弹幕 id，多个以逗号分隔"
                },
                "comment": "是否已点赞弹幕"
            },
            "send_danmaku": {
                "url": "https://api.bilibili.com/x/v2/dm/post",
                "method": "POST",
                "verify": true,
                "data": {
                    "type": "const int: 1",
                    "oid": "int: 分 P 编号",
                    "msg": "int: 弹幕内容",
                    "bvid": "int: bvid",
                    "progress": "int: 发送时间（毫秒）",
                    "color": "int: 颜色（十六进制转十进制）",
                    "fontsize": "int: 字体大小（小 18 普通 25 大 36）",
                    "pool": "int bool: 字幕弹幕（1 是 0 否）",
                    "mode": "int: 模式（滚动 1 顶部 5 底部 4）",
                    "plat": "const int: 1"
                },
                "comment": "发送弹幕"
            },
            "like_danmaku": {
                "url": "https://api.bilibili.com/x/v2/dm/thumbup/add",
                "method": "POST",
                "verify": true,
                "data": {
                    "dmid": "int: 弹幕 ID",
                    "oid": "int: 分 P 编号",
                    "op": "int: 1 点赞 2 取消点赞",
                    "platform": "const str: web_player"
                },
                "comment": "点赞弹幕"
            },
            "edit_danmaku": {
                "url": "https://api.bilibili.com/x/v2/dm/edit/state",
                "method": "POST",
                "verify": true,
                "data": {
                    "type": "const int: 1",
                    "dmids": "int: 弹幕 ID",
                    "oid": "int: 视频 cid",
                    "state": "int: 1 删除 2 保护 3 取消保护"
                },
                "comment": "编辑弹幕"
            },
            "snapshot": {
                "url": "http://api.bilibili.com/x/v2/dm/ajax",
                "method": "GET",
                "verify": false,
                "params": {
                    "aid": "int or string: av 号或 BV 号"
                },
                "comment": "获取弹幕快照"
            },
            "recall": {
                "url": "http://api.bilibili.com/x/dm/recall",
                "method": "GET",
                "verify": false,
                "data": {
                    "dmid": "int: 弹幕 ID",
                    "cid": "int: 分 P 编号",
                    "csrf": "cookies: bili_jct"
                },
                "comment": "撤回弹幕"
            }
        }
    },
    "user": {
        "info": {
            "name_to_uid": {
                "url": "https://api.vc.bilibili.com/dynamic_mix/v1/dynamic_mix/name_to_uid",
                "method": "GET",
                "verify": false,
                "params": {
                    "names": "string: 多个名称, 用,分割"
                }
            },
            "my_info": {
                "url": "https://api.bilibili.com/x/space/myinfo",
                "method": "GET",
                "verify": true,
                "comment": "获取自己的信息"
            },
            "info": {
                "url": "https://api.bilibili.com/x/space/acc/info",
                "method": "GET",
                "verify": false,
                "params": {
                    "mid": "int: uid"
                },
                "comment": "用户基本信息"
            },
            "space_notice": {
                "url": "http://api.bilibili.com/x/space/notice",
                "method": "GET",
                "verify": false,
                "params": {
                    "mid": "int: uid"
                },
                "comment": "用户个人空间公告"
            },
            "user_tag": {
                "url": "http://space.bilibili.com/ajax/tags/getSubList",
                "method": "GET",
                "verify": false,
                "params": {
                    "mid": "int: uid"
                },
                "comment": "用户关注的 TAG / 话题,认证方式：SESSDATA"
            },
            "user_top_videos": {
                "url": "https://api.bilibili.com/x/space/top/arc",
                "method": "GET",
                "verify": false,
                "params": {
                    "vmid": "int: uid"
                },
                "comment": "用户代表作"
            },
            "relation": {
                "url": "https://api.bilibili.com/x/relation/stat",
                "method": "GET",
                "verify": false,
                "params": {
                    "vmid": "int: uid"
                },
                "comment": "关注数，粉丝数"
            },
            "upstat": {
                "url": "https://api.bilibili.com/x/space/upstat",
                "method": "GET",
                "verify": false,
                "params": {
                    "mid": "int: uid"
                },
                "comment": "视频播放量，文章阅读量，总点赞数"
            },
            "user_medal": {
                "url": "https://api.live.bilibili.com/xlive/web-ucenter/user/MedalWall",
                "method": "GET",
                "verify": true,
                "params": {
                    "target_id": "int: uid"
                },
                "comment": "读取用户粉丝牌详细信息，如果隐私则不可以"
            },
            "live": {
                "url": "https://api.bilibili.com/x/space/acc/info",
                "method": "GET",
                "verify": false,
                "params": {
                    "mid": "int: uid"
                },
                "comment": "直播间基本信息"
            },
            "video": {
                "url": "https://api.bilibili.com/x/space/arc/search",
                "method": "GET",
                "verify": false,
                "params": {
                    "mid": "int: uid",
                    "ps": "const int: 30",
                    "tid": "int: 分区 ID，0 表示全部",
                    "pn": "int: 页码",
                    "keyword": "str: 关键词，可为空",
                    "order": "str: pubdate 上传日期，pubdate 播放量，pubdate 收藏量"
                },
                "comment": "搜索用户视频"
            },
            "reservation": {
                "url": "https://api.bilibili.com/x/space/reservation",
                "method": "GET",
                "verify": false,
                "params": {
                    "vmid": "int: uid"
                },
                "comment": "获取用户空间预约"
            },
            "album": {
                "url": "https://api.vc.bilibili.com/link_draw/v1/doc/doc_list",
                "method": "GET",
                "verify": false,
                "params": {
                    "uid": "int: uid 此项必须",
                    "page_size": "int: 每页项数 此项必须",
                    "page_num": "int: 页码",
                    "biz": "str: 全部：all 绘画：draw 摄影：photo 日常：daily 默认为 all"
                },
                "comment": "相簿"
            },
            "audio": {
                "url": "https://api.bilibili.com/audio/music-service/web/song/upper",
                "method": "GET",
                "verify": false,
                "params": {
                    "uid": "int: uid",
                    "ps": "const int: 30",
                    "pn": "int: 页码",
                    "order": "int: 1 最新发布，2 最多播放，3 最多收藏"
                },
                "comment": "音频"
            },
            "article": {
                "url": "https://api.bilibili.com/x/space/article",
                "method": "GET",
                "verify": false,
                "params": {
                    "mid": "int: uid",
                    "ps": "const int: 30",
                    "pn": "int: 页码",
                    "sort": "str: publish_time 最新发布，publish_time 最多阅读，publish_time 最多收藏"
                },
                "comment": "专栏"
            },
            "article_lists": {
                "url": "https://api.bilibili.com/x/article/up/lists",
                "method": "GET",
                "verify": false,
                "params": {
                    "mid": "int: uid",
                    "sort": "int: 0 最近更新，1 最多阅读"
                },
                "comment": "专栏文集"
            },
            "dynamic": {
                "url": "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history",
                "method": "GET",
                "verify": false,
                "params": {
                    "host_uid": "int: uid",
                    "offset_dynamic_id": "int: 动态偏移用，第一页为 0",
                    "need_top": "int bool: 是否显示置顶动态"
                },
                "comment": "用户动态信息"
            },
            "bangumi": {
                "url": "https://api.bilibili.com/x/space/bangumi/follow/list",
                "method": "GET",
                "verify": false,
                "params": {
                    "vmid": "int: uid",
                    "pn": "int: 页码",
                    "ps": "const int: 15",
                    "type": "int: 1 追番，2 追剧"
                },
                "comment": "用户追番列表"
            },
            "followings": {
                "url": "https://api.bilibili.com/x/relation/followings",
                "method": "GET",
                "verify": true,
                "params": {
                    "vmid": "int: uid",
                    "ps": "const int: 20",
                    "pn": "int: 页码",
                    "order": "str: desc 倒序, asc 正序"
                },
                "comment": "获取用户关注列表（不是自己只能访问前 5 页）"
            },
            "all_followings": {
                "url": "https://account.bilibili.com/api/member/getCardByMid",
                "method": "GET",
                "verify": false,
                "params": {
                    "mid": "int: uid"
                },
                "comment": "获取用户所有关注（需要用户公开信息）"
            },
            "all_followings2": {
                "url": "https://app.biliapi.net/x/v2/relation/followings",
                "method": "GET",
                "verify": false,
                "params": {
                    "vmid": "int: uid",
                    "pn": "int: 页码",
                    "ps": "const int: 100"
                },
                "comment": "获取用户关注"
            },
            "followers": {
                "url": "https://api.bilibili.com/x/relation/followers",
                "method": "GET",
                "verify": true,
                "params": {
                    "vmid": "int: uid",
                    "ps": "const int: 20",
                    "pn": "int: 页码",
                    "order": "str: desc 倒序, asc 正序"
                },
                "comment": "获取用户粉丝列表（不是自己只能访问前 5 页，是自己也不能获取全部的样子）"
            },
            "top_followers": {
                "url": "https://member.bilibili.com/x/web/data/fan",
                "method": "GET",
                "verify": false,
                "params": {
                    "t": "int: since when in timestamp(msec)",
                    "csrf,csrf_token": "要给两个"
                },
                "comment": "粉丝排行"
            },
            "overview": {
                "url": "https://api.bilibili.com/x/space/navnum",
                "method": "GET",
                "verify": false,
                "params": {
                    "mid": "int: uid",
                    "jsonp": "const str: jsonp"
                },
                "comment": "获取用户的简易订阅和投稿信息(主要是这些的数量统计)"
            },
            "self_subscribe_group": {
                "url": "https://api.bilibili.com/x/relation/tags",
                "method": "GET",
                "verify": true,
                "params": {},
                "comment": "获取自己的关注分组列表，用于操作关注"
            },
            "get_user_in_which_subscribe_groups": {
                "url": "https://api.bilibili.com/x/relation/tag/user",
                "method": "GET",
                "verify": true,
                "params": {
                    "fid": "int: uid"
                },
                "comment": "获取用户在哪一个分组"
            },
            "history": {
                "url": "https://api.bilibili.com/x/v2/history",
                "method": "GET",
                "verify": true,
                "params": {
                    "pn": "int: 页码",
                    "ps": "const int: 100"
                },
                "comment": "用户浏览历史记录"
            },
            "channel_list": {
                "url": "https://api.bilibili.com/x/polymer/space/seasons_series_list",
                "method": "GET",
                "verity": false,
                "params": {
                    "mid": "int: uid",
                    "page_num": "int: 开始项",
                    "page_size": "int: 开始项后面的项数"
                },
                "comment": "查看用户合集的列表（新版）"
            },
            "channel_video_series": {
                "url": "https://api.bilibili.com/x/series/archives",
                "method": "GET",
                "verity": false,
                "params": {
                    "mid": "int: uid",
                    "series_id": "int: series_id",
                    "pn": "int: 页码",
                    "ps": "const int: 100"
                },
                "comment": "查看列表内视频（旧版）"
            },
            "channel_video_season": {
                "url": "https://api.bilibili.com/x/polymer/space/seasons_archives_list",
                "method": "GET",
                "verity": false,
                "params": {
                    "mid": "int: uid",
                    "season_id": "int: season_id",
                    "sort_reverse": "bool: 是否升序排序，否则默认排序",
                    "page_num": "int: 页码",
                    "page_size": "int: 每一页的项数"
                },
                "comment": "查看用户合集中的视频（新版）"
            },
            "pugv": {
                "url": "https://api.bilibili.com/pugv/app/web/season/page",
                "method": "GET",
                "verity": false,
                "params": {
                    "mid": "int: uid"
                },
                "comment": "查看用户的课程"
            },
            "get_coins": {
                "url": "https://account.bilibili.com/site/getCoin",
                "method": "GET",
                "verify": true,
                "comment": "获取硬币数量"
            },
            "events": {
                "url": "https://member.bilibili.com/x2/creative/h5/calendar/event",
                "method": "GET",
                "params": {
                    "ts": "int: 时间戳"
                },
                "verify": true,
                "comment": "获取事件"
            }
        },
        "operate": {
            "modify": {
                "url": "https://api.bilibili.com/x/relation/modify",
                "method": "POST",
                "verify": true,
                "data": {
                    "fid": "int: UID",
                    "act": "int: 1 关注 2 取关 3 悄悄关注 5 拉黑 6 取消拉黑 7 移除粉丝",
                    "re_src": "const int: 11"
                },
                "comment": "用户关系操作"
            },
            "del_channel_aids_series": {
                "url": "https://api.bilibili.com/x/series/series/delArchives",
                "method": "POST",
                "verity": true,
                "params": {
                    "mid": "int: uid",
                    "series_id": "int: series_id",
                    "aids": "int: aid 列表"
                }
            },
            "set_space_notice": {
                "url": "http://api.bilibili.com/x/space/notice/set",
                "method": "POST",
                "verify": true,
                "params": {
                    "notice": "str: text ,不必要",
                    "csrf": "str: CSRF Token（位于 cookie），必要"
                },
                "comment": "修改用户个人空间公告"
            },
            "del_channel_series": {
                "url": "https://api.bilibili.com/x/series/series/delete",
                "method": "POST",
                "verity": true,
                "query": {
                    "mid": "int: uid",
                    "series_id": "int: series_id",
                    "aids": "list: 所有 aid 列表",
                    "csrf": "string: bili_jct 的值"
                }
            },
            "create_subscribe_group": {
                "url": "https://api.bilibili.com/x/relation/tag/create",
                "method": "POST",
                "verify": true,
                "data": {
                    "tag": "str: 分组名"
                },
                "comment": "添加关注分组"
            },
            "del_subscribe_group": {
                "url": "https://api.bilibili.com/x/relation/tag/del",
                "method": "POST",
                "verify": true,
                "data": {
                    "tagid": "int: 分组 id"
                },
                "comment": "删除关注分组"
            },
            "rename_subscribe_group": {
                "url": "https://api.bilibili.com/x/relation/tag/update",
                "method": "POST",
                "verify": true,
                "data": {
                    "tagid": "int: 分组 id",
                    "name": "str: 新的分组名"
                },
                "comment": "重命名分组"
            },
            "set_user_subscribe_group": {
                "url": "https://api.bilibili.com/x/relation/tags/addUsers",
                "method": "POST",
                "verify": true,
                "data": {
                    "fids": "int: UID",
                    "tagids": "commaSeparatedList[int]: 分组的 tagids，逗号分隔"
                },
                "comment": "移动用户到关注分组"
            }
        }
    }
}
