from torrents.pirate_bay import PirateBay
from torrents.x1337 import x1337


def check_if_site_available(site):
    all_sites = {
        "1337x": {
            "website": x1337,
            "trending_available": True,
            "trending_category": True,
            "search_by_category": True,
            "recent_available": True,
            "recent_category_available": True,
            "categories": [
                "anime",
                "music",
                "games",
                "tv",
                "apps",
                "documentaries",
                "other",
                "xxx",
                "movies",
            ],
            "limit": 10,
        },
        "piratebay": {
            "website": PirateBay,
            "trending_available": True,
            "trending_category": False,
            "search_by_category": False,
            "recent_available": True,
            "recent_category_available": True,
            "categories": ["tv"],
            "limit": 50,
        }
    }

    if site in all_sites.keys():
        return all_sites
    return False
