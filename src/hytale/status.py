from .http import get
from .models.status import Status


def get_status() -> Status:
    data = get("/status")
    return Status(data)
