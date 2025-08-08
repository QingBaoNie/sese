from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.core.star.filter.event_message_type import EventMessageType
import random
from .back import time_long, volume


@register("sese", "Qing", "撸一下插件", "1.0.0", "https://github.com/QingBaoNie/sese")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    # 监听群聊和私聊的文本消息
    @filter.event_message_type(EventMessageType.GROUP_MESSAGE)
    async def on_group_message(self, event: AstrMessageEvent):
        msg = event.message_str.strip()
        if msg == "撸一下":
            await self._do_lu(event)

    @filter.event_message_type(EventMessageType.PRIVATE_MESSAGE)
    async def on_private_message(self, event: AstrMessageEvent):
        msg = event.message_str.strip()
        if msg == "撸一下":
            await self._do_lu(event)

    async def _do_lu(self, event: AstrMessageEvent):
        time_val = round(random.uniform(1, 600), 2)
        V = round(random.uniform(0.01, 100), 2)
        a = time_long(time_val)
        b = volume(V)
        user_name = event.get_sender_name()
        await event.plain_result(
            f"{user_name}，你坚持了 {time_val}s哦，{a} 射出 {V}ml，{b}!"
        )
