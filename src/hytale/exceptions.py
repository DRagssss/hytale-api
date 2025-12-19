class HytaleAPIError(Exception):
    """Base exception for Hytale API errors."""


class BlockedError(HytaleAPIError):
    """Exception for when access is blocked by Cloudflare."""
