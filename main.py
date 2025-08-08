from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import random
from .back import time_long, volume

@register(
    name="撸一下",  # 插件唯一识别名
    author="Qing",  # 作者
    description="这是 AstrBot 的插件",  # 插件简短描述
    version="v1.0",  # 插件版本
    help="撸一下",  # 插件帮助信息
    repo="https://github.com/QingBaoNie/sese"  # 插件仓库地址
)
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @filter.message()
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
