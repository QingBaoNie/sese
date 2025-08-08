import random
import time
from datetime import datetime
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.core.star.filter.event_message_type import EventMessageType
from .back import time_long, volume


@register("sese", "Qing", "撸一下插件", "1.0.1", "https://github.com/QingBaoNie/sese")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.last_time = {}        # {user_id: 上次执行时间戳}
        self.daily_count = {}      # {user_id: 今日次数}
        self.last_reset_day = self._today_str()  # 上次重置日期

    def _today_str(self):
        return datetime.now().strftime("%Y-%m-%d")

    def _reset_if_new_day(self):
        """跨天自动清空次数"""
        today = self._today_str()
        if today != self.last_reset_day:
            self.daily_count.clear()
            self.last_reset_day = today

    @filter.event_message_type(EventMessageType.GROUP_MESSAGE)
    async def on_group_message(self, event: AstrMessageEvent):
        msg = event.message_str.strip()
        if msg == "撸一下":
            yield self._do_lu(event)

    @filter.event_message_type(EventMessageType.PRIVATE_MESSAGE)
    async def on_private_message(self, event: AstrMessageEvent):
        msg = event.message_str.strip()
        if msg == "撸一下":
            yield self._do_lu(event)

    def _do_lu(self, event: AstrMessageEvent) -> MessageEventResult:
        user_id = event.get_sender_id()
        now = time.time()

        # 跨天检测并重置次数
        self._reset_if_new_day()

        # 每日次数限制
        count = self.daily_count.get(user_id, 0)
        if count >= 2:
            return event.plain_result("今天你已经撸够两次了，留点体力明天再来~")

        # 冷却检测（60 秒）
        if user_id in self.last_time and now - self.last_time[user_id] < 60:
            return event.plain_result("你小子，这么频繁想阳痿是吗？")

        # 记录本次时间和次数
        self.last_time[user_id] = now
        self.daily_count[user_id] = count + 1

        # 生成随机结果
        time_val = round(random.uniform(1, 600), 2)
        V = round(random.uniform(0.01, 100), 2)

        # 时间单位转换
        if time_val < 60:
            time_str = f"{time_val}秒"
        elif time_val < 3600:
            time_str = f"{round(time_val / 60, 1)}分钟"
        else:
            time_str = f"{round(time_val / 3600, 2)}小时"

        a = time_long(time_val)
        b = volume(V)
        user_name = event.get_sender_name()

        return event.plain_result(
            f"{user_name}，你坚持了 {time_str}哦，{a} 射出 {V}ml，{b}!"
        )
