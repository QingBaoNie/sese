from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.core.star.filter.event_message_type import event_message_type, EventMessageType
from astrbot.core.platform.sources.aiocqhttp.aiocqhttp_message_event import AiocqhttpMessageEvent as AstrMessageEvent
import random
from .back import time_long, volume

@register(
    "sese",  # 插件识别名
    "Qing",  # 作者
    "撸一下",  # 描述
    "v1.0",  # 版本
    "https://github.com/QingBaoNie/sese"  # 仓库
)
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    # 监听群聊消息
    @event_message_type(EventMessageType.GROUP_MESSAGE)
    async def on_group_message(self, event: AstrMessageEvent):
        msg = event.message_str.strip()
        if msg == "撸一下":
            time_val = round(random.uniform(1, 600), 2)
            V = round(random.uniform(0.01, 100), 2)
            a = time_long(time_val)
            b = volume(V)
            user_name = event.get_sender_name()
            yield event.plain_result(
                f"{user_name}，你撸了 {time_val}s，{a} 射出了 {V}ml，{b}!"
            )
