from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.event import filter
from astrbot.api.event.message_event import AstrMessageEvent
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

    @filter.event()
    async def on_message(self, event: AstrMessageEvent):
        """
        兼容老版本 AstrBot 的消息监听
        """
        # 只处理群聊消息
        if getattr(event.message_obj, "message_type", None) != "group":
            return

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
