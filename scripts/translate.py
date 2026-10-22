
from beet import Context, Language

TRANSLATIONS = {
    "dialog.more-confirm.confirm": ("确认", "Confirm"),
    "dialog.more-confirm.back": ("返回", "Back"),
    "dialog.more-confirm.title": ("", ""),
    "dialog.more-confirm.body.title": ("\n确认执行操作", "\nConfirm Action"),
    "dialog.more-confirm.body.contents": (
        "你尝试执行的操作需要较高权限。\n这可能会对游戏产生负面影响。\n确定要执行吗？\n§e操作：%s\n",
        "The action you are attempting to perform requires elevated privileges.\nThis may negatively affect the game.\nAre you sure you want to proceed?\n§eAction: %s\n"
    ),
    "dialog.more-confirm.body.with.block_use": ("方块交互", "Interact with Block"),
    "dialog.more-confirm.body.with.bred_animals": ("繁殖动物", "Breed Animals"),
    "dialog.more-confirm.body.with.brewed_potion": ("酿造药水", "Brew Potion"),
    "dialog.more-confirm.body.with.changed_dimension": ("改变维度", "Change Dimension"),
    "dialog.more-confirm.body.with.channeled_lightning": ("引雷", "Channel Lightning"),
    "dialog.more-confirm.body.with.construct_beacon": ("激活信标", "Activate Beacon"),
    "dialog.more-confirm.body.with.consume_item": ("消耗物品", "Consume Item"),
    "dialog.more-confirm.body.with.crafter_crafted": ("合成器喷出物品", "Craft Item with Crafter"),
    "dialog.more-confirm.body.with.effects_changed": ("改变状态效果", "Change Status Effects"),
    "dialog.more-confirm.body.with.enchanted_item": ("附魔", "Enchant Item"),
    "dialog.more-confirm.body.with.enter_block": ("进入方块内部", "Enter Block"),
    "dialog.more-confirm.body.with.fall_after_explosion": ("被爆炸冲击后下落", "Fall After Explosion"),
    "dialog.more-confirm.body.with.fall_from_height": ("摔落到地面", "Fall from Height"),
    "dialog.more-confirm.body.with.filled_bucket": ("填充铁桶", "Fill Bucket"),
    "dialog.more-confirm.body.with.fishing_rod_hooked": ("通过钓鱼获取物品", "Catch Item with Fishing Rod"),
    "dialog.more-confirm.body.with.hero_of_the_village": ("袭击胜利", "Defeat Raid"),
    "dialog.more-confirm.body.with.inventory_changed": ("物品栏变化", "Change Inventory"),
    "dialog.more-confirm.body.with.item_durability_changed": ("物品耐久变化", "Change Item Durability"),
    "dialog.more-confirm.body.with.kill_mob_near_sculk_catalyst": ("在幽匿催发体旁击杀生物", "Kill Mob Near Sculk Catalyst"),
    "dialog.more-confirm.body.with.killed_by_arrow": ("用箭杀死生物", "Kill Entity with Arrow"),
    "dialog.more-confirm.body.with.hit_block": ("挖掘方块", "Mine Block"),
    "dialog.more-confirm.body.with.placed_block": ("放置方块", "Place Block"),
    "dialog.more-confirm.body.with.move_backward": ("向后走", "Move Backward"),
    "dialog.more-confirm.body.with.move_forward": ("向前走", "Move Forward"),
    "dialog.more-confirm.body.with.move_jump": ("跳跃", "Jump"),
    "dialog.more-confirm.body.with.move_left": ("向左走", "Move Left"),
    "dialog.more-confirm.body.with.move_right": ("向右走", "Move Right"),
    "dialog.more-confirm.body.with.move_sneak": ("潜行", "Sneak"),
    "dialog.more-confirm.body.with.move_sprint": ("疾跑", "Sprint"),
    "dialog.more-confirm.body.with.look_at": ("看向实体", "Look at Entity"),
    "dialog.more-confirm.body.with.levitation": ("处于飘浮状态", "Levitate"),
    "dialog.more-confirm.body.with.lightning_strike": ("闪电束消失", "Lightning Bolt Disappears"),
    "dialog.more-confirm.body.with.location": ("每秒更新", "Update Every Second"),
    "dialog.more-confirm.body.with.player_generates_container_loot": ("开启战利品箱", "Open Loot Container"),
    "dialog.more-confirm.body.with.player_hurt_entity": ("攻击生物", "Attack Entity"),
    "dialog.more-confirm.body.with.player_interacted_with_entity": ("与生物交互", "Interact with Entity"),
    "dialog.more-confirm.body.with.player_killed_entity": ("击杀生物", "Kill Entity"),
    "dialog.more-confirm.body.with.player_sheared_equipment": ("剪下生物装备", "Shear Entity Equipment"),
    "dialog.more-confirm.body.with.recipe_crafted": ("合成物品", "Craft Item"),
    "dialog.more-confirm.body.with.recipe_unlocked": ("解锁配方", "Unlock Recipe"),
    "dialog.more-confirm.body.with.ride_entity_in_lava": ("在熔岩上骑乘实体", "Ride Entity on Lava"),
    "dialog.more-confirm.body.with.shot_crossbow": ("使用弩射击", "Fire Crossbow"),
    "dialog.more-confirm.body.with.slept_in_bed": ("在床上睡觉", "Sleep in Bed"),
    "dialog.more-confirm.body.with.slide_down_block": ("从方块侧边滑下", "Slide Down Block"),
    "dialog.more-confirm.body.with.started_riding": ("开始骑乘", "Start Riding"),
    "dialog.more-confirm.body.with.summoned_entity": ("召唤实体", "Summon Entity"),
    "dialog.more-confirm.body.with.spear_mobs": ("进行冲锋攻击", "Perform Charge Attack"),
    "dialog.more-confirm.body.with.tame_animal": ("驯服动物", "Tame Animal"),
    "dialog.more-confirm.body.with.target_hit": ("击中标靶", "Hit Target"),
    "dialog.more-confirm.body.with.thrown_item_picked_up_by_entity": ("实体捡起你扔出的物品", "Entity Picks Up Thrown Item"),
    "dialog.more-confirm.body.with.thrown_item_picked_up_by_player": ("捡起实体扔出的物品", "Pick Up Item Thrown by Entity"),
    "dialog.more-confirm.body.with.used_ender_eye": ("使用末影之眼", "Use Eye of Ender"),
    "dialog.more-confirm.body.with.used_totem": ("触发不死图腾", "Activate Totem of Undying"),
    "dialog.more-confirm.body.with.villager_trade": ("与村民交易", "Trade with Villager"),
    "dialog.more-confirm.body.with.voluntary_exile": ("触发袭击", "Trigger Raid"),
}


def beet_default(ctx: Context):
    for index, language in enumerate(("more-confirm:zh_cn", "more-confirm:en_us")):
        ctx.assets[f"{language}"] = Language({
            key: values[index]
            for key, values in TRANSLATIONS.items()
        })