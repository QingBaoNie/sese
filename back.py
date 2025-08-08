import random

# 时长评价（谐音 + 暗示 + 隐喻版）
def time_long(time):
    openings = [
        "艹，才动两下就GG？",
        "哼，这么快就交卷？",
        "哦？秒收小王子~",
        "嘻嘻，小废D，",
        "哈，这耐力也太…"
    ]
    insults = [
        "你这小J连暖场都撑不住。",
        "活该被nv生笑得捂嘴。",
        "你这种续航，别说冲，暖手都嫌累。",
        "下次直接跪着开单机吧。",
        "还没到终点，喷泉就开了。"
    ]
    mid = [
        "嗯，还想多冲几下啊？",
        "唔~ 再加点力度？",
        "好嘛，今天勉强能多冲一会儿。",
        "小D稍微硬气了点，继续~"
    ]
    praise = [
        "不错，能让我双次high才GG。",
        "好样的，把我冲到腿软。",
        "嗯嗯~ 就这样，把‘奶油’送进来。",
        "再顶几下，把我冲到冒泡。"
    ]
    beast = [
        "卧槽，你这牲口级续航是想冲到我断片吗？",
        "继续！冲到我喊不出来为止！",
        "啊啊啊！你这是要把我搞趴下吗！",
        "你是想让我第二天废掉吗？"
    ]

    if time < 3:
        return random.choice(openings) + random.choice(insults)
    elif time < 20:
        return random.choice(openings) + random.choice(insults)
    elif time < 40:
        return random.choice(mid) + random.choice(insults)
    elif time < 80:
        return random.choice(mid)
    elif time < 150:
        return random.choice(praise)
    elif time < 300:
        return random.choice(praise)
    elif time < 500:
        return random.choice(praise) + " " + random.choice(beast)
    else:
        return random.choice(beast)


# 量评价（谐音 + 暗示 + 隐喻版）
def volume(V):
    tiny = [
        "哈？就这？像水龙头漏水一样，根本不够抹。",
        "这点料，抹在手背上都不湿。",
        "小废D，你这点‘奶’连缝都塞不满。"
    ]
    small = [
        "这点‘奶’，我抿一口就没了。",
        "勉强够我抹在小豆上打转。",
        "哼，下次多攒几天再来冲。"
    ]
    medium = [
        "嗯~ 把小窝灌得暖暖的。",
        "‘奶油’热乎乎地全进来了。",
        "小窝都被你的‘奶’灌满了。"
    ]
    big = [
        "好家伙，流得我大腿全是。",
        "床单都湿透了，你是攒了一个星期的量吧？",
        "我里面全是白乎乎的，走路都要溢出来。"
    ]
    huge = [
        "我去，这量像倒牛奶！",
        "喷得我身上全是！",
        "你这牲口是奶厂转世吗？！"
    ]

    if V < 1:
        return random.choice(tiny)
    elif V < 3:
        return random.choice(tiny + small)
    elif V < 10:
        return random.choice(small)
    elif V < 20:
        return random.choice(small + medium)
    elif V < 50:
        return random.choice(medium)
    elif V < 80:
        return random.choice(big)
    else:
        return random.choice(huge)
