from datetime import datetime

import attrs

from ..base import FromDictMixin


@attrs.define(slots=True)
class Media(FromDictMixin):
    _id: str = attrs.field(alias="_id")
    category: str
    src: str
    createdAt: datetime
    weight = int

    @classmethod
    def from_dict(cls, data):
        data = dict(data)
        if "createdAt" in data:
            data["createdAt"] = datetime.fromisoformat(data["createdAt"])
        return super().from_dict(data)
