import json

from pydantic.dataclasses import dataclass

from bot.settings import settings


@dataclass
class _Messages:
    start: str


class Dispatcher:
    messages: _Messages


def dispatcher_init():
    with open(settings.messages_file, "r", encoding="utf-8") as file:
        Dispatcher.messages = _Messages(**json.load(file))
