from datetime import datetime
from typing import Dict

version = "1.4.4"

INDEX_ENDPOINT = "https://beta-api.crunchyroll.com/index/v2"
PROFILE_ENDPOINT = "https://beta-api.crunchyroll.com/accounts/v1/me/profile"
TOKEN_ENDPOINT = "https://beta-api.crunchyroll.com/auth/v1/token"
SEARCH_ENDPOINT = "https://beta-api.crunchyroll.com/content/v1/search"
STREAMS_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/videos/{}/streams"
SERIES_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/series/{}"
SEASONS_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/seasons"
EPISODES_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/episodes"
SIMILAR_ENDPOINT = "https://beta-api.crunchyroll.com/content/v1/{}/similar_to"
NEWSFEED_ENDPOINT = "https://beta-api.crunchyroll.com/content/v1/news_feed"
BROWSE_ENDPOINT = "https://beta-api.crunchyroll.com/content/v1/browse"
OBJECTS_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/objects/{}"

AUTHORIZATION = (
    "Basic d2piMV90YThta3Y3X2t4aHF6djc6MnlSWlg0Y0psX28yMzRqa2FNaXRTbXNLUVlGaUpQXzU="
)

PLAYLIST_REG = r"\#EXT\-X\-STREAM\-INF\:BANDWIDTH\=(\d+)\,RESOLUTION\=(\d+)x(\d+)"


def headers() -> Dict:
    return {
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Crunchyroll/3.59.0 Android/14 okhttp/4.12.0",
    }

def fixup(d: Dict):
    if "" in d:
        d["raw"] = d[""]
        d.pop("")
    for v in d.values():
        if isinstance(v, dict):
            fixup(v)


def get_date() -> datetime:
    return datetime.utcnow()


def date_to_str(date: datetime) -> str:
    return "{}-{}-{}T{}:{}:{}Z".format(
        date.year, date.month, date.day, date.hour, date.minute, date.second
    )


def str_to_date(string: str) -> datetime:
    return datetime.strptime(string, "%Y-%m-%dT%H:%M:%SZ")
