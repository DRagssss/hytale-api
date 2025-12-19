from .http import get
from .models.media.image import Image
from .models.media.video import Video


def get_screenshots() -> list[Image]:
    data = get("/media/category/screenshots")
    return [Image.from_dict(item) for item in data]


def get_desktop_wallpapers() -> list[Image]:
    data = get("/media/category/desktopWallpapers")
    return [Image.from_dict(item) for item in data]


def get_mobile_wallpapers() -> list[Image]:
    data = get("/media/category/mobileWallpapers")
    return [Image.from_dict(item) for item in data]


def get_concept_arts() -> list[Image]:
    data = get("/media/category/conceptArt")
    return [Image.from_dict(item) for item in data]


def get_videos() -> list[Video]:
    data = get("/media/category/videos")
    return [Video.from_dict(item) for item in data]
