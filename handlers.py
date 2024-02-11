from PIL import Image
import json, datetime

id = ''

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
    # прокси лист - переменная для получения карточки
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
            return hashMap

    if hashMap.get("listener")=="CardsClick":
        geted = hashMap.get("selected_card_key")
        dt_now = datetime.datetime.now()
        format = str(geted).replace("'", "\"")
        test = json.loads(format)

        test['date'] = str(dt_now.strftime('%Y-%m-%d-%H:%M:%S'))
    
        id = str(test)
        return hashMap


def birds_seen(hashMap,_files=None,_data=None):
    global id
    
    cards = { "customcards":         {
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
            },
            {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@date",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": ""
            },
            ]

            },
            
            ]
        },
        ]
    }

}
}   
    
    data = json.loads(id.replace("'", "\""))
    with open ('/storage/emulated/0/Android/data/ru.travelfood.simple_ui/files/text1.json', 'w', encoding='utf-8') as text:
            json.dump(data, text, ensure_ascii=False)
    cards["customcards"]["cardsdata"]=[]
    commit =  {
    "key": str(data),
    "name": data["name"],
    "desc": data['desc'],
    "image": data['image'],
    "date": data['date']}

    cards["customcards"]["cardsdata"].append(commit)

    hashMap.put("cards1",json.dumps(cards,ensure_ascii=False).encode('utf8').decode())
    return hashMap