from typing import Dict, List
from pydantic import BaseModel, Field

class PlaylistItem(BaseModel):
    url: str = Field(default=None)
    bandwidth: int = Field(default=None)
    width: int = Field(default=None)
    height: int = Field(default=None)
    framerate: str = Field(default=None)
    codecs: str = Field(default=None)

class Image(BaseModel):
    width: int = Field(default=None)
    height: int = Field(default=None)
    type: str = Field(default=None)
    source: str = Field(default=None)

class Images(BaseModel):
    poster_tall: List[List[Image]] = Field(default=None)
    poster_wide: List[List[Image]] = Field(default=None)
    thumbnail: List[List[Image]] = Field(default=None)

class SeriesMetadata(BaseModel):
    availability_notes: str = Field(default=None)
    episode_count: int = Field(default=None)
    extended_description: str = Field(default=None)
    is_dubbed: bool = Field(default=None)
    is_mature: bool = Field(default=None)
    is_simulcast: bool = Field(default=None)
    is_subbed: bool = Field(default=None)
    mature_blocked: bool = Field(default=None)
    maturity_ratings: List[str] = Field(default=None)
    season_count: int = Field(default=None)

class SearchMetadata(BaseModel):
    score: int = Field(default=None)

class Link(BaseModel):
    href: str = Field(default=None)

class NewsItems(BaseModel):
    title: str = Field(default=None)
    link: str = Field(default=None)
    image: str = Field(default=None)
    creator: str = Field(default=None)
    publish_date: str = Field(default=None)
    description: str = Field(default=None)

class News(BaseModel):
    total: int = Field(default=None)
    items: List[NewsItems] = Field(default=None)

class Series(BaseModel):
    id: str = Field(default=None)
    channel_id: str = Field(default=None)
    title: str = Field(default=None)
    slug: str = Field(default=None)
    slug_title: str = Field(default=None)
    description: str = Field(default=None)
    extended_description: str = Field(default=None)
    keywords: List[str] = Field(default=None)
    season_tags: List[str] = Field(default=None)
    images: Images = Field(default=None)
    maturity_ratings: List[str] = Field(default=None)
    episode_count: int = Field(default=None)
    season_count: int = Field(default=None)
    media_count: int = Field(default=None)
    content_provider: str = Field(default=None)
    is_mature: bool = Field(default=None)
    mature_blocked: bool = Field(default=None)
    is_subbed: bool = Field(default=None)
    is_dubbed: bool = Field(default=None)
    is_simulcast: bool = Field(default=None)
    seo_title: str = Field(default=None)
    seo_description: str = Field(default=None)
    availability_notes: str = Field(default=None)

class Panel(BaseModel):
    channel_id: str = Field(default=None)
    description: str = Field(default=None)
    external_id: str = Field(default=None)
    id: str = Field(default=None)
    type: str = Field(default=None)
    images: Images = Field(default=None)
    last_public: str = Field(default=None)
    linked_resource_key: str = Field(default=None)
    new: bool = Field(default=None)
    new_content: bool = Field(default=None)
    promo_description: str = Field(default=None)
    promo_title: str = Field(default=None)
    search_metadata: SearchMetadata = Field(default=None)
    series_metadata: SeriesMetadata = Field(default=None)
    slug: str = Field(default=None)
    slug_title: str = Field(default=None)
    title: str = Field(default=None)

class Collection(BaseModel):
    type: str = Field(default=None)
    total: int = Field(default=None)
    items: List[Panel] = Field(default=None)

class NewsFeed(BaseModel):
    top_news: News = Field(default=None)
    latest_news: News = Field(default=None)

class Season(BaseModel):
    id: str = Field(default=None)
    channel_id: str = Field(default=None)
    title: str = Field(default=None)
    slug_title: str = Field(default=None)
    series_id: str = Field(default=None)
    season_number: int = Field(default=None)
    is_complete: bool = Field(default=None)
    description: str = Field(default=None)
    keywords: List[str] = Field(default=None)
    season_tags: List[str] = Field(default=None)
    images: Dict = Field(default=None)
    is_mature: bool = Field(default=None)
    mature_blocked: bool = Field(default=None)
    is_subbed: bool = Field(default=None)
    is_dubbed: bool = Field(default=None)
    is_simulcast: bool = Field(default=None)
    seo_title: str = Field(default=None)
    seo_description: str = Field(default=None)
    availability_notes: str = Field(default=None)

class EpisodeLinks(BaseModel):
    channel: Link = Field(default=None, alias="episode/channel")
    next_episode: Link = Field(default=None, alias="episode/next_episode")
    season: Link = Field(default=None, alias="episode/season")
    series: Link = Field(default=None, alias="episode/series")
    streams: Link = Field(default=None)

class Episode(BaseModel):
    links: EpisodeLinks = Field(default=None, alias="__links__")
    id: str = Field(default=None)
    channel_id: str = Field(default=None)
    series_id: str = Field(default=None)
    series_title: str = Field(default=None)
    season_id: str = Field(default=None)
    season_title: str = Field(default=None)
    season_number: int = Field(default=None)
    episode: str = Field(default=None)
    episode_number: int = Field(default=None)
    sequence_number: int = Field(default=None)
    production_episode_id: str = Field(default=None)
    title: str = Field(default=None)
    slug_title: str = Field(default=None)
    description: str = Field(default=None)
    next_episode_id: str = Field(default=None)
    next_episode_title: str = Field(default=None)
    hd_flag: bool = Field(default=None)
    is_mature: bool = Field(default=None)
    mature_blocked: bool = Field(default=None)
    episode_air_date: str = Field(default=None)
    is_subbed: bool = Field(default=None)
    is_dubbed: bool = Field(default=None)
    is_clip: bool = Field(default=None)
    seo_title: str = Field(default=None)
    seo_description: str = Field(default=None)
    season_tags: List[str] = Field(default=None)
    available_offline: bool = Field(default=None)
    media_type: str = Field(default=None)
    slug: str = Field(default=None)
    images: Images = Field(default=None)
    duration_ms: int = Field(default=None)
    is_premium_only: bool = Field(default=None)
    listing_id: str = Field(default=None)
    subtitle_locales: List[str] = Field(default=None)
    playback: str = Field(default=None)
    availability_notes: str = Field(default=None)

class StreamData(BaseModel):
    hardsub_locale: str = Field(default=None)
    url: str = Field(default=None)

class SubtitleData(BaseModel):
    locale: str = Field(default=None)
    url: str = Field(default=None)
    format: str = Field(default=None)

class VideoFormat(BaseModel):
    raw: StreamData = Field(default=None)
    en: StreamData = Field(default=None, alias="en-US")
    es: StreamData = Field(default=None, alias="es-ES")
    es_la: StreamData = Field(default=None, alias="es-LA")
    pt_br: StreamData = Field(default=None, alias="pt-BR")
    pt: StreamData = Field(default=None, alias="pt-PT")
    fr: StreamData = Field(default=None, alias="fr-FR")
    de: StreamData = Field(default=None, alias="de-DE")
    ar: StreamData = Field(default=None, alias="ar-SA")
    it: StreamData = Field(default=None, alias="it-IT")
    ru: StreamData = Field(default=None, alias="ru-RU")

class Subtitles(BaseModel):
    en: SubtitleData = Field(default=None, alias="en-US")
    es_la: SubtitleData = Field(default=None, alias="es-LA")
    es: SubtitleData = Field(default=None, alias="es-ES")
    pt_br: SubtitleData = Field(default=None, alias="pt-BR")
    pt: SubtitleData = Field(default=None, alias="pt-PT")
    fr: SubtitleData = Field(default=None, alias="fr-FR")
    de: SubtitleData = Field(default=None, alias="de-DE")
    ar: SubtitleData = Field(default=None, alias="ar-SA")
    it: SubtitleData = Field(default=None, alias="it-IT")
    ru: SubtitleData = Field(default=None, alias="ru-RU")

class Streams(BaseModel):
    adaptive_dash: VideoFormat = Field(default=None)
    adaptive_hls: VideoFormat = Field(default=None)
    drm_adaptive_dash: VideoFormat = Field(default=None)
    drm_adaptive_hls: VideoFormat = Field(default=None)
    drm_multitrack_adaptive_hls_v2: VideoFormat = Field(default=None)
    multitrack_adaptive_hls_v2: VideoFormat = Field(default=None)
    vo_adaptive_dash: VideoFormat = Field(default=None)
    vo_adaptive_hls: VideoFormat = Field(default=None)
    vo_drm_adaptive_dash: VideoFormat = Field(default=None)
    vo_drm_adaptive_hls: VideoFormat = Field(default=None)

class StreamsInfo(BaseModel):
    media_id: str = Field(default=None)
    audio_locale: str = Field(default=None)
    subtitles: Subtitles = Field(default=None)
    streams: Streams = Field(default=None)
    bifs: List[str] = Field(default=None)