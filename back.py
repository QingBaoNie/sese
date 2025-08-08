import random

# 射精时长评价（超露骨 + 随机化）
def time_long(time):
    openings = [
        "艹，才插两下就射？",
        "哼，这么快就缴械？",
        "哦？秒射狗~",
        "嘻嘻，小废屌，",
        "哈，这耐力？"
    ]
    insults = [
        "你这小鸡巴连前戏都撑不住。",
        "活该被女人笑得合不拢腿。",
        "你这种耐力，别说操，舔都嫌累。",
        "下次直接跪着打飞机吧。",
        "你这速度，还没插进子宫就崩了。"
    ]
    mid = [
        "嗯，还想多顶几下啊？",
        "唔~ 再用力插插？",
        "好嘛，今天勉强能多操几下。",
        "鸡巴稍微硬了一点，继续~"
    ]
    praise = [
        "不错，能让我高潮两次才射。",
        "好样的，把我操得小穴一阵阵痉挛。",
        "嗯嗯~ 就这样，把精液射我深处。",
        "再顶几下，把逼干到喷水。"
    ]
    beast = [
        "卧槽，你这牲口级耐力是想把我操到昏过去吗？",
        "继续！操到我喊不出来为止！",
        "啊啊啊！你他妈要把我操烂了！",
        "你是想让我下半身报废吗？"
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


# 精液量评价（超露骨 + 随机化）
def volume(V):
    tiny = [
        "哈？就这？像漏尿一样，根本不够我舔。",
        "这点量，抹在乳头上都湿不了。",
        "小废屌，你这点精液连手指缝都塞不满。"
    ]
    small = [
        "这点精液，我抿一口就没了。",
        "勉强够我抹在阴蒂上玩玩。",
        "哼，下次多攒几天再来操。"
    ]
    medium = [
        "嗯~ 把逼里灌得暖暖的。",
        "精液热乎乎地全射在我深处。",
        "小穴都被你的精液灌满了。"
    ]
    big = [
        "好家伙，精液流得我大腿全是。",
        "床单都湿透了，你是存了一个星期的量吧？",
        "我逼里全是白乎乎的，走路都要流出来。"
    ]
    huge = [
        "我操，这量像倒牛奶！",
        "精液喷得我肚子和脸上全是！",
        "你这牲口是精液工厂转世吗？！"
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
