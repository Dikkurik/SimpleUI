from PIL import Image
import json, random, os

birds = {"birds":[
    {
    "name":"Снегирь",
    "image":"images/snegir.jpg",
    "desc":"Это Снегирь",
    "status": "False"
    }
    ,
    {
        "name":"Чайка",
        "image":"images/chaika.jpg",
        "desc":"Это Чайка",
        "status": "False"
    }
    ,
    {
        "name":"Ласточка",
        "image":"images/snegir.jpg",
        "desc":"Это Снегирь",
        "status": "False"
    }
]
}



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

            [{
            "type": "Picture",
            "show_by_condition": "",
            "Value": "@pic",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": "",
            "TextSize": "16",
            "TextColor": "#DB7093",
            "TextBold": True,
            "TextItalic": False,
            "BackgroundColor": "",
            "width": "match_parent",
            "height": "wrap_content",
            "weight": 2
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
                "width": "50",
                "height": "50",
                "weight": 0
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
    # with open('db.json', encoding='utf-8') as db:
    #     db = json.load(db)
    # print(db['birds'])
    j["customcards"]["cardsdata"]=[]
    for i in birds['birds']:
        commit =  {
        "key": str(i),
        "name": i["name"],
        "desc": i['desc'],
        "image": i['image']
    }
        j["customcards"]["cardsdata"].append(commit)

    with open('test.txt', 'w', encoding='utf-8') as file:
            file.write(str(j))

    hashMap.put("cards",json.dumps(j,ensure_ascii=False).encode('utf8').decode())

    return hashMap


def input_data(hashMap,_files=None,_data=None):
  if hashMap.get("listener")=="btn_post":
      "name"
      hashMap.put("toast",str(int(hashMap.get("a"))+int(hashMap.get("b"))))

  return hashMap

def test_inp(name:str, desc:str):
    with open ('db.json', encoding='utf-8') as db:
        db = json.load(db)
        target = db["birds"]
        print(target)
        commit = {"name": name,
                  "desc": desc}
        db["birds"].append(commit)
    
        print(f'Добавлено{name},{desc} ', db)
    pass

test_inp('Куртца', 'Это курица')