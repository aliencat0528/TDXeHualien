import sys
import json
sys.path.append("C:\\herokuenv\\eHualien")
#print(sys.path)

#from django.conf import settings
from eHualien import settings
from linebot import LineBotApi
from linebot.models import * #TextSendMessage,ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction,LocationAction
from CollectData import parkAPI
from tdxDemo import richmenu

line_bot_api=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def sendPark(event):
    try:
        data = parkAPI.DealData(
            ['https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/CarPark/City/HualienCounty?%24format=JSON',
            'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingEntranceExit/City/HualienCounty?%24format=JSON',
            'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingAvailability/City/HualienCounty?%24format=JSON']

        )
        data.getData()
        parkinfo = data.parkInfo("parkavailable")
        print(parkinfo)

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

def shareUsrLoc(event):
    try:
        message=TextSendMessage(text="點選按鈕以分享位置",quick_reply=QuickReply(items=[QuickReplyButton(action=LocationAction(label="開啟地圖"))]))
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

def getNearPark(event):
    try:
        #print("緯度:"+str(event.message.latitude)+"\n"+"經度:"+str(event.message.longitude))
        nearpark=parkAPI.DealLoc(event.message.latitude,event.message.longitude)
        cntDistPark=nearpark.cntDistance()
        findnear=nearpark.getNearInfo(cntDistPark)
        fiveNear=findnear[0]
        fiveNameAddr = findnear[1]
        oriSortData=findnear[2]

        print("testsort:",type(fiveNameAddr),fiveNameAddr)
        # message=TextSendMessage(text=fiveNear,quick_reply=QuickReply(items=[QuickReplyButton(action=PostbackAction(label="開啟按鈕",data="123"))]))
        message = TextSendMessage(text=fiveNear, quick_reply=QuickReply(
            items=[QuickReplyButton(action=PostbackAction(label=">>資料傳送門請點我<<", data=str(fiveNameAddr),display_text='可以打開路線規劃搜尋囉~'))]))
        #message=TextSendMessage(text="緯度:"+str(event.message.latitude)+"\n"+"經度:"+str(event.message.longitude))
        line_bot_api.reply_message(event.reply_token,message)
        #getParam(nearpark.getNearToGo(cntDistPark))

    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

def sendGoPlan(event):
    try:

        print("test:",event)
        message = TemplateSendMessage(
            alt_text='停車場路徑規劃',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='停車場名字1',
                        text='停車地址1',
                        actions=[URITemplateAction(label="開啟地圖",uri='https://www.google.com/maps/dir/?api=1')]),
                    CarouselColumn(
                        title='停車場名字2',
                        text='停車地址2',
                        actions=[URITemplateAction(label="開啟地圖",uri='https://www.google.com/maps/dir/?api=1')]),
                    CarouselColumn(
                        title='停車場名字3',
                        text='停車地址3',
                        actions=[URITemplateAction(label="開啟地圖", uri='https://www.google.com/maps/dir/?api=1')]),
                    CarouselColumn(
                        title='停車場名字4',
                        text='停車地址4',
                        actions=[URITemplateAction(label="開啟地圖", uri='https://www.google.com/maps/dir/?api=1')]),
                    CarouselColumn(
                        title='停車場名字5',
                        text='停車地址5',
                        actions=[URITemplateAction(label="開啟地圖", uri='https://www.google.com/maps/dir/?api=1')])
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))

# def testparam(event,*parkargs):
#     print("park:",parkargs)
#     parkAPI.DealShowInfo(parkargs)


def setQuery(event,**parkargs):
    try:
        global abctest

        abctest=["aaaaaaa","bbbbbb","cccccc","ddddddd"]
        print("eeeee:",event)
        if(event.type=='postback'):
            global testdata
            testdata = []
            print("456456456")
            print("testargs:",parkargs)
            test = parkAPI.DealShowInfo(passparg=parkargs['pargs'])
            print("backargs:",test.testrlt())
            testdata.append(test.testrlt())
            print("testdata:",testdata[0])
        elif(event.type=='message'):
            print("123123123")
            print("testpasssucc:",str(testdata[0]))
            message = TextSendMessage(text=str(testdata[0]))
            line_bot_api.reply_message(event.reply_token, message)
        else:
            pass
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))

# def changeMenu(usrid,datamsg):
#     pass

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
