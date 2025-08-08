from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import random
from .back import time_long, volume

@register("helloworld", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @event_message_type(EventMessageType.GROUP_MESSAGE)  # 监听群聊消息
    async def dajiao(self, event: AstrMessageEvent):
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
