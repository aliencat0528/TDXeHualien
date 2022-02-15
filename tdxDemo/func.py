from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage,StickerSendMessage,\
    LocationSendMessage,QuickReply,QuickReplyButton,MessageAction
from CollectData.parkAPI import DealData

line_bot_api=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendPark(event):
    try:
        parkinfo=DealData.showInfo()
        message=TextSendMessage(text=parkinfo)
        line_bot_api.reply_message(event.reply_token,message)
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
        message=TextSendMessage(text="789")
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
