advancement revoke @s only more-confirm:summoned_entity

dialog show @s {\
    title:"",\
    type:"multi_action",\
    columns:2,\
    body:[\
        {type:"plain_message",contents:{translate:"dialog.more-confirm.body.title"}},\
        {type:"plain_message",contents:[{"translate":"dialog.more-confirm.body.contents",\
        "with":[{"translate":"dialog.more-confirm.body.with.summoned_entity",color:yellow}]}]},\
    ],\
    actions:[\
        {label:{translate:"dialog.more-confirm.confirm"}},\
        {label:{translate:"dialog.more-confirm.back"}}\
    ]\
}