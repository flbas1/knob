from typing import TypedDict#, Literal

class Payload(TypedDict):
    # type: Literal["Payload"]
    screen: str
    selected: int

class LauncherPayload(TypedDict):
    # type: Literal["launcher"]
    selected: int
    items: list[str]


class VolumePayload(TypedDict):
    # type: Literal["volume"]
    value: int
    muted: bool


class MediaPayload(TypedDict):
    # type: Literal["media"]
    title: str
    artist: str
    position: int
    duration: int    