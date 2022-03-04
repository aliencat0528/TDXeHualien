import sys
import json
sys.path.append("C:\\herokuenv\\eHualien")
#print(sys.path)

from django.conf import settings
from linebot import LineBotApi
from linebot.models import * #TextSendMessage,ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction,LocationAction
from CollectData import parkAPI

line_bot_api=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def sendPark(event):
    try:
        data = parkAPI.DealData(
            ['https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingEntranceExit/City/HualienCounty?%24format=JSON',
            'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingAvailability/City/HualienCounty?%24format=JSON']

        )
        data.getData()
        parkinfo = data.parkInfo("parkavailable")
        #print(parkinfo)

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
        message=TextSendMessage(text="點選按鈕以分享位置",quick_reply=QuickReply(items=[QuickReplyButton(action=LocationAction(label="開啟地圖"))]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

def getUsrLoc(event):
    try:
        #print("緯度:"+str(event.message.latitude)+"\n"+"經度:"+str(event.message.longitude))
        #distance=parkAPI.DealData.cntDistance(event.message.latitude,event.message.longitude)
        message=TextSendMessage(text="緯度:"+str(event.message.latitude)+"\n"+"經度:"+str(event.message.longitude))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

# if __name__ == '__main__':
#       nearinfo = parkAPI.DealLoc(25.030094, 121.557377)
#       nearinfo.getNearInfo()
#       print(nearinfo)
#     data = parkAPI.DealData(
#         [
#             'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingEntranceExit/City/HualienCounty?%24format=JSON',
#             'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingAvailability/City/HualienCounty?%24format=JSON']
#
#     )
#     data.getData()
#     parkinfo = data.parkInfo("parkavailable")
#     print(parkinfo)
