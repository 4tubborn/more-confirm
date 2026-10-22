
from beet import Context, Function, Advancement

TRIGGERS = [
    "allay_drop_item_on_block",
    "any_block_use",
    "avoid_vibration",
    "bee_nest_destroyed",
    "bred_animals",
    "brewed_potion",
    "changed_dimension",
    "channeled_lightning",
    "construct_beacon",
    "consume_item",
    "crafter_recipe_crafted",
    "cured_zombie_villager",
    "default_block_use",
    "effects_changed",
    "enchanted_item",
    "enter_block",
    "entity_hurt_player",
    "entity_killed_player",
    "fall_after_explosion",
    "fall_from_height",
    "filled_bucket",
    "fishing_rod_hooked",
    "hero_of_the_village",
    "impossible",
    "inventory_changed",
    "item_durability_changed",
    "item_used_on_block",
    "kill_mob_near_sculk_catalyst",
    "killed_by_arrow",
    "levitation",
    "lightning_strike",
    "location",
    "nether_travel",
    "placed_block",
    "player_generates_container_loot",
    "player_hurt_entity",
    "player_interacted_with_entity",
    "player_killed_entity",
    "player_sheared_equipment",
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
    "tick",
    "used_ender_eye",
    "used_totem",
    "using_item",
    "villager_trade",
    "voluntary_exile",
]

# 保留定义，但不生成这些触发器的进度
DISABLED_TRIGGERS = {
    "impossible",
    "tick",
}

SCORE_TRIGGERS = {
    "location": 1,
}

TEMPLATE_FUNC = """advancement revoke @s only more-confirm:{name}

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


def beet_default(ctx: Context):

    ctx.data["more-confirm:_load_"] = Function(
        "scoreboard objectives add more-confirm.type dummy"
    )

    for name in TRIGGERS:
        resource_id = f"more-confirm:{name}"

        # 生成函数
        ctx.data[resource_id] = Function(
            TEMPLATE_FUNC.format(name=name).splitlines()
        )

        # 生成进度条件
        criterion = {
            "trigger": f"minecraft:{name}"
        }

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

        # 生成进度
        ctx.data.advancements[resource_id] = Advancement({
            "criteria": {
                "use": criterion
            },
            "rewards": {
                "function": resource_id
            }
        })
