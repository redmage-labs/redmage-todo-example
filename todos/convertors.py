from typing import Optional

from starlette.convertors import Convertor


class OptionalInt(Convertor):
    regex = "[0-9]+|None"

    def convert(self, value: str) -> Optional[int]:
        return int(value) if value != "None" else None

    def to_string(self, value: Optional[int]) -> str:
        return str(value) if value else "None"
