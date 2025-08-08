import random

# 时长评价（谐音 + 暗示版）
def time_long(time):
    openings = [
        "艹，才动两下就交械？",
        "哼，这么快就GG？",
        "哦？秒社小王子~",
        "嘻嘻，小废D，",
        "哈，这耐力？"
    ]
    insults = [
        "你这小J连前戏都撑不住。",
        "活该被nv人笑得合不拢嘴。",
        "你这种耐力，别说冲，舔都嫌累。",
        "下次直接跪着用手吧。",
        "你这速度，还没到终点就喷了。"
    ]
    mid = [
        "嗯，还想多冲几下啊？",
        "唔~ 再用力一点？",
        "好嘛，今天勉强能多坚持几下。",
        "小D稍微硬了一点，继续~"
    ]
    praise = [
        "不错，能让我爽两次才GG。",
        "好样的，把我冲到腿软。",
        "嗯嗯~ 就这样，把‘奶油’送进来。",
        "再顶几下，把我冲到爆。"
    ]
    beast = [
        "卧槽，你这牲口级耐力是想把我冲晕过去吗？",
        "继续！冲到我喊不出来为止！",
        "啊啊啊！你这是要把我搞废吗！",
        "你是想让我第二天下不了床吗？"
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


# 量评价（谐音 + 暗示版）
def volume(V):
    tiny = [
        "哈？就这？像漏水一样，根本不够抹。",
        "这点料，抹在手上都不湿。",
        "小废D，你这点‘奶’连手指缝都塞不满。"
    ]
    small = [
        "这点‘奶’，我抿一口就没了。",
        "勉强够我抹在小豆上玩玩。",
        "哼，下次多攒几天再来冲。"
    ]
    medium = [
        "嗯~ 把里面灌得暖暖的。",
        "‘奶油’热乎乎地全进来了。",
        "小窝都被你的‘奶’灌满了。"
    ]
    big = [
        "好家伙，流得我腿全是。",
        "床单都湿透了，你是攒了一个星期的量吧？",
        "我里面全是白乎乎的，走路都要流出来。"
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
