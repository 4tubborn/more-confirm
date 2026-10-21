import json
from pathlib import Path
from typing import Any

NAMESPACE = "more-confirm"

FUNC_DIR = Path("data") / NAMESPACE / "function"
ADV_DIR = Path("data") / NAMESPACE / "advancement"

# 完整触发器列表
triggers = [
    "bee_nest_destroyed",
    "lightning_strike",
    "location",
    "player_generates_container_loot",
    "player_hurt_entity",
    "player_interacted_with_entity",
    "player_killed_entity",
    "player_sheared_equipment",
    "recipe_crafted",
    "recipe_unlocked",
    "ride_entity_in_lava",
    "shot_crossbow",
    "slept_in_bed",
    "slide_down_block",
    "started_riding",
    "summoned_entity",
    "spear_mobs",
    "tame_animal",
    "target_hit",
    "thrown_item_picked_up_by_entity",
    "thrown_item_picked_up_by_player",
    "used_ender_eye",
    "used_totem",
    "using_item",
    "villager_trade",
    "voluntary_exile"
]

# 需要添加计分板条件的触发器
# 值为允许触发的最小分数
SCORE_TRIGGERS = {
    "location": 1,
}

# mcfunction 模板
template_func = """advancement revoke @s only more-confirm:{name}

dialog show @s {{\\
    title:"",\\
    type:"multi_action",\\
    columns:2,\\
    body:[\\
        {{type:"plain_message",contents:{{translate:"dialog.more-confirm.body.title"}}}},\\
        {{type:"plain_message",contents:[{{translate:"dialog.more-confirm.body.contents",\\
        with:[{{translate:"dialog.more-confirm.body.with.{name}",color:yellow}}]}}]}},\\
    ],\\
    actions:[\\
        {{label:{{translate:"dialog.more-confirm.confirm"}}}},\\
        {{label:{{translate:"dialog.more-confirm.back"}}}}\\
    ]\\
}}"""


def generate():
    FUNC_DIR.mkdir(parents=True, exist_ok=True)
    ADV_DIR.mkdir(parents=True, exist_ok=True)

    for name in triggers:
        # 生成 mcfunction
        func_path = FUNC_DIR / f"{name}.mcfunction"

        func_content = template_func.format(name=name)

        func_path.write_text(
            func_content,
            encoding="utf-8"
        )

        # 构造进度触发器
        criterion = {
            "trigger": f"minecraft:{name}"
        }

        # 按需添加计分板条件
        if name in SCORE_TRIGGERS:
            criterion["conditions"] = {
                "player": [
                    {
                        "condition": "minecraft:entity_scores",
                        "entity": "this",
                        "scores": {
                            "more-confirm.type": {
                                "min": SCORE_TRIGGERS[name]
                            }
                        }
                    }
                ]
            }

        # 构造进度 JSON
        advancement = {
            "criteria": {
                "use": criterion
            },
            "rewards": {
                "function": f"{NAMESPACE}:{name}"
            }
        }

        # 写入进度文件
        adv_path = ADV_DIR / f"{name}.json"

        adv_path.write_text(
            json.dumps(
                advancement,
                indent=4,
                ensure_ascii=False
            ) + "\n",
            encoding="utf-8"
        )

    print(f"成功！生成了 {2 * len(triggers)} 个文件。")


if __name__ == "__main__":
    generate()