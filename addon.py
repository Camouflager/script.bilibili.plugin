import xbmc
import xbmcgui
import workflows
import traceback
from bilibili import UserException


opts = [
    {
        "label": "Default Search",
        "workflow": workflows.DefaultSearch.start
    },
    {
        "label": "Search Users",
        "workflow": workflows.SearchUser.start
    },
    {
        "label": "Top Hits",
        "workflow": workflows.TopHits.start
    },
    {
        "label": "Recent History",
        "workflow": workflows.RecentHistory.start
    },
    {
        "label": "Default Quality",
        "workflow": workflows.DefaultVideoQuality.start
    },
]


def main():

    while True:
        selectedIndex = xbmcgui.Dialog().select('Bilibili', [x["label"] for x in opts])

        if selectedIndex < 0:
            break

        ret = opts[selectedIndex]["workflow"]()

        if ret == 'fin':
            break

    workflows.RecentHistory.writeFile()


try:
    main()
except UserException as e:
    xbmcgui.Dialog().ok('err', str(e))
except Exception as e:
    st = traceback.format_exc()
    xbmc.log('exception: ' + str(st), xbmc.LOGERROR)
    xbmcgui.Dialog().textviewer('err', str(st))
