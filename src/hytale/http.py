import json

import requests

from ._version import __version__
from .exceptions import BlockedError, HytaleAPIError

BASE_URL = "hytale.com/api"
DEFAULT_USER_AGENT = (
    f"hytale-api/{__version__} (+https://github.com/DRagssss/hytale-api)"
)

_session = requests.Session()
_session.headers.update(
    {
        "User-Agent": DEFAULT_USER_AGENT,
        "Accept": "application/json",
    }
)


def get(path: str, sub_domain: str = "", **params) -> dict | str:
    url = "https://" + sub_domain + BASE_URL + path

    print(url)

    try:
        response = _session.get(
            url,
            params=params,
            timeout=3,
        )
    except requests.RequestException as exc:
        raise HytaleAPIError(str(exc)) from exc

    if not response.ok:
        if "Attention Required! | Cloudflare" in response.text:
            raise BlockedError("This IP is blocked")
        raise HytaleAPIError(
            f"Request failed [{response.status_code}]: {response.text}"
        )

    try:
        return json.loads(response.text)
    except json.decoder.JSONDecodeError:
        return response.text
