from astrbot.api.event import filter
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.event import AstrMessageEvent
import random
from .back import time_long, volume

@register("sese", "Qing", "撸一下插件", "1.0.0", "https://github.com/QingBaoNie/sese")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.text()  # 监听所有文本消息
    async def on_text_message(self, event: AstrMessageEvent):
        msg = event.message_str.strip()
        if msg == "撸一下":  # 纯文本触发
            time_val = round(random.uniform(1, 600), 2)
            V = round(random.uniform(0.01, 100), 2)
            a = time_long(time_val)
            b = volume(V)
            user_name = event.get_sender_name()
            yield event.plain_result(
                f"{user_name}，你坚持了 {time_val}s哦，{a} 射出 {V}ml，{b}!"
            )
