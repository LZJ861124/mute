
from __future__ import annotations

from typing import Type

from component.name import Name
from component.role import Role

from event.event import Event
from message.message import Message
from system.channel import Channel

from logcat.logcat import LogCat

class CmdEcho:
    @LogCat.log_func
    def __init__(self, servant: Type[Handler]):
        servant.on(Event.CMD_ECHO, self._on_cmd_echo)

    @LogCat.log_func
    def _on_cmd_echo(
        self, e: Event, entity: str = '', args: str = ''
    ) -> None:
        if not args:
            text = f'Echo : ？'

            Channel.toRole(entity, Message.TEXT, text)
        else:
            text = f'Echo：{" ".join(args)}'

            role = Role.instance(entity)
            Channel.toRoom(role.room, Message.TEXT, text)

# cmd_say.py
