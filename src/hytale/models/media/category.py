from enum import Enum


class Category(Enum):
    screenshots = "screenshots"
    desktopWallpapers = "desktopWallpapers"
    mobileWallpapers = "mobileWallpapers"
    conceptArt = "conceptArt"
    videos = "videos"

    def _prefixed(self) -> str:
        name = self.name
        if name[-1] == "s":
            name = name[:-1]  # Remove trailing 's'

        snake_str = ""
        for i, char in enumerate(name):
            if char.isupper():
                if i != 0:
                    snake_str += "_"
                snake_str += char.lower()
            else:
                snake_str += char
        return snake_str

    def prefixed(self) -> str:
        if self.name == "screenshots":
            return ""
        else:
            return self._prefixed() + "_"
