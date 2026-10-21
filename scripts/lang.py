import json
from pathlib import Path

# 触发器名称与中文描述的映射表
translation_map = {
    "bee_nest_destroyed": "破坏蜂巢/蜂箱",
    "levitation": "处于飘浮状态",
    "lightning_strike": "闪电消失",
    "location": "每秒更新",
    "placed_block": "放置方块",
    "player_generates_container_loot": "开启战利品箱",
    "player_hurt_entity": "攻击生物",
    "player_interacted_with_entity": "与生物交互",
    "player_killed_entity": "击杀生物",
    "player_sheared_equipment": "剪下生物装备",
    "recipe_crafted": "合成物品",
    "recipe_unlocked": "解锁配方",
    "ride_entity_in_lava": "在熔岩上骑乘实体",
    "shot_crossbow": "使用弩射击",
    "slept_in_bed": "在床上睡觉",
    "slide_down_block": "从方块侧边滑下",
    "started_riding": "开始骑乘",
    "summoned_entity": "召唤实体",
    "spear_mobs": "进行冲锋攻击",
    "tame_animal": "驯服动物",
    "target_hit": "击中标靶",
    "thrown_item_picked_up_by_entity": "实体捡起你扔出的物品",
    "thrown_item_picked_up_by_player": "捡起实体扔出的物品",
    "used_ender_eye": "使用末影之眼",
    "used_totem": "触发不死图腾",
    "villager_trade": "与村民交易",
    "voluntary_exile": "触发袭击"
}

def generate_lang_file():
    lang_data = {
        f"dialog.more-confirm.body.with.{key}": value
        for key, value in translation_map.items()
    }

    path = Path("resourcepack/assets/minecraft/lang/zh_cn.json")

    # 创建父目录，而不是 JSON 文件本身
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        json.dumps(
            lang_data,
            indent=4,
            ensure_ascii=False
        ) + "\n",
        encoding="utf-8"
    )

    print(f"成功！语言文件已生成为: {path}")
    print(f"共生成了 {len(lang_data)} 个翻译条目。")


if __name__ == "__main__":
    generate_lang_file()