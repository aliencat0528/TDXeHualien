import sys

sys.path.append("C:\\herokuenv\\eHualien")
#print(sys.path)

from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction,LocationAction
from CollectData import parkAPI

line_bot_api=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendPark(event):
    try:
        data = parkAPI.DealData(
            'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingEntranceExit/City/HualienCounty?%24format=JSON',
            'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingAvailability/City/HualienCounty?%24format=JSON'

        )
        data.getData()
        parkinfo = data.showInfo("parkavailable")
        # print(parkinfo)
        message = TextSendMessage(text=str(parkinfo))
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

def sendRealTraffic(event):
    try:
        message=TextSendMessage(text="456")
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

def sendGoPlan(event):
    try:
        message=TextSendMessage(quick_reply=QuickReply(items=[QuickReplyButton(action=LocationAction(label="開啟地圖分享位置"))]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
