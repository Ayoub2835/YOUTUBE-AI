"""Resolves a platform name to its publisher implementation."""

from __future__ import annotations

from storygen.config import Settings, get_settings
from storygen.publishing.base import BasePublisher


def get_publisher(platform: str, settings: Settings | None = None) -> BasePublisher:
    settings = settings or get_settings()
    platform = platform.lower()

    if platform == "youtube":
        from storygen.publishing.youtube_publisher import YouTubePublisher

        return YouTubePublisher(settings)
    if platform == "tiktok":
        from storygen.publishing.tiktok_publisher import TikTokPublisher

        return TikTokPublisher(settings)
    if platform == "snapchat":
        from storygen.publishing.snapchat_publisher import SnapchatPublisher

        return SnapchatPublisher(settings)

    raise ValueError(f"No publisher available for platform '{platform}'.")
