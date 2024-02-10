from PIL import Image
import json

id = []

def birds_on_start(hashMap,_files=None,_data=None):
    j = { "customcards":         {
        "options":{
          "search_enabled":True,
          "save_position":True
        },

        "layout": {


        "type": "LinearLayout",
        "orientation": "vertical",
        "height": "match_parent",
        "width": "match_parent",
        "weight": "0",
        "Elements": [
        {
            "type": "LinearLayout",
            "orientation": "horizontal",
            "height": "wrap_content",
            "width": "match_parent",
            "weight": "0",
            "Elements": 

            [            {   
                "type": "Picture",
                "show_by_condition": "",
                "Value": "@image",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "",
                "TextSize": "16",
                "TextColor": "#DB7093",
                "TextBold": True,
                "TextItalic": False,
                "BackgroundColor": "",
                "width": "75",
                "height": "75",
                "weight": 0
            },
            {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "wrap_content",
            "width": "match_parent",
            "weight": "1",
            "Elements": 

            [{
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@name",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": ""
            },
            {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@desc",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": ""
            }]

            },
            ]
        },

        {
            "type": "TextView",
            "show_by_condition": "",
            "Value": "@desc",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": "",
            "TextSize": "-1",
            "TextColor": "#6F9393",
            "TextBold": False,
            "TextItalic": True,
            "BackgroundColor": "",
            "width": "wrap_content",
            "height": "wrap_content",
            "weight": 0
        }
        ]
    }

}
}   
    with open('/storage/emulated/0/Android/data/ru.travelfood.simple_ui/files/db.json', encoding='utf-8') as db:
        birds = json.load(db)
    print(birds['birds'])
    j["customcards"]["cardsdata"]=[]
    for i in birds['birds']:
        commit =  {
        "key": str(i),
        "name": i["name"],
        "desc": i['desc'],
        "image": i['image']
    }
        j["customcards"]["cardsdata"].append(commit)

    hashMap.put("cards",json.dumps(j,ensure_ascii=False).encode('utf8').decode())

    return hashMap


def input_data(hashMap,_files=None,_data=None):
    global id
    proxy_list = []
    if hashMap.get("listener")=="btn_post":
        with open ('/storage/emulated/0/Android/data/ru.travelfood.simple_ui/files/db.json', encoding='utf-8') as db:
            db = json.load(db)
        commit = { 
                    'id': str(len(db['birds'])),
                    "name": hashMap.get("input_name"),
                    "desc": hashMap.get("input_desc"),
                    "image": hashMap.get("photo"),
                    "status": "false"}
        db["birds"].append(commit)
        with open('/storage/emulated/0/Android/data/ru.travelfood.simple_ui/files/db.json', 'w', encoding='utf-8') as fp:
            json.dump(db, fp, ensure_ascii=False)

    if hashMap.get("listener")=="CardsClick":
        id = hashMap.get("selected_card_key")
        proxy_list.append(id)
        with open ('/storage/emulated/0/Android/data/ru.travelfood.simple_ui/files/text.json', 'w', encoding='utf-8') as text:
            json.dump(proxy_list, text, ensure_ascii=False)
        with open ('/storage/emulated/0/Android/data/ru.travelfood.simple_ui/files/db.json', encoding='utf-8') as db:
            db = json.load(db)
        db_pos = db["birds"][id]