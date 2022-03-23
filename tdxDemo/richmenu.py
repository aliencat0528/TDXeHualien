import sys
import json
import requests

sys.path.append("C:\\herokuenv\\eHualien")
from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.models import RichMenu,RichMenuArea,RichMenuSize,RichMenuBounds,PostbackAction,URIAction,MessageAction
# from linebot.models.actions import RichMenuSwitchAction
# from linebot.models.rich_menu import RichMenuAlias

line_bot_api=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser=WebhookParser(settings.LINE_CHANNEL_SECRET)

def homePage():
    func={
      "size": {
        "width": 2500,
        "height": 843
      },
      "selected": 'true',
      "name": "主畫面選單",
      "chatBarText": "就從這裡出發吧!!",
      "areas": [
        {
          "bounds": {
            "x": 0,
            "y": 0,
            "width": 830,
            "height": 843
          },
          "action": {
            "type": "postback",
            #"text": "停車",
            "data": "switchPark"
          }
        },
        {
          "bounds": {
            "x": 840,
            "y": 0,
            "width": 830,
            "height": 843
          },
          "action": {
            "type": "message",
            "text": "路況待開發"
          }
        },
        {
          "bounds": {
            "x": 1680,
            "y": 0,
            "width": 830,
            "height": 843
          },
          "action": {
            "type": "message",
            "text": "商家待開發"
          }
        }
      ]
    }
    homeMenuID=setMenu(func)
    with open('C:/herokuenv/eHualien/tdxDemo/home.png','rb') as f1:
      line_bot_api.set_rich_menu_image(homeMenuID,'image/png',f1)


def subPark():
    parkfunc={
      "size": {
        "width": 2500,
        "height": 1686
      },
      "selected": 'false',
      "name": "停車子選單",
      "chatBarText": "多的是~你不知道的事lol",
      "areas": [
        {
          "bounds": {
            "x": 280,
            "y": 50,
            "width": 1000,
            "height": 750
          },
          "action": {
            "type": "message",
            "text": "我附近的停車場在哪呢?"
          }
        },
        {
          "bounds": {
            "x": 1400,
            "y": 50,
            "width": 1000,
            "height": 750
          },
          "action": {
            "type": "message",
            "text": "指引我方向吧!!"
          }
        },
        {
          "bounds": {
            "x": 280,
            "y": 900,
            "width": 1000,
            "height": 750
          },
          "action": {
            "type": "message",
            "text": "今天我想查點.."
          }
        },
        {
          "bounds": {
            "x": 1400,
            "y": 900,
            "width": 1000,
            "height": 750
          },
          "action": {
            "type": "message",
            "text": "還有多少車位呢?"
          }
        },
        {
          "bounds": {
            "x": 20,
            "y": 10,
            "width": 260,
            "height": 260
          },
          "action": {
            "type": "postback",
            #"text": "返回主頁",
            "data": "switchHome"
          }
        }
      ]
    }
    parkMenuID=setMenu(parkfunc)
    with open('C:/herokuenv/eHualien/tdxDemo/newpark.png','rb') as f2:
        line_bot_api.set_rich_menu_image(parkMenuID,'image/png',f2)


def createAction(action):
  if action['type']=='postback':
    return PostbackAction(data=action['data'])
  else:
    return MessageAction(text=action['text'])

def setMenu(funset):
  area=[
    RichMenuArea(
      bounds=RichMenuBounds(
        x=f['bounds']['x'],
        y=f['bounds']['y'],
        width=f['bounds']['width'],
        height=f['bounds']['height']
      ),
      action=createAction(f['action'])
    ) for f in funset['areas']
  ]

  createMenu=RichMenu(
    size=RichMenuSize(
      width=funset['size']['width'],
      height=funset['size']['height']
    ),
    selected=funset['selected'],
    name=funset['name'],
    chat_bar_text=funset['chatBarText'],
    areas=area

  )
  menuID=line_bot_api.create_rich_menu(rich_menu=createMenu)
  print(menuID)
  return menuID

if __name__ == '__main__':
    homePage()
    subPark()
