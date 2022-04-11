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

        #print("testsort:",type(fiveNameAddr),fiveNameAddr)
        #stepback=sendGoPlan(event='none', lat=event.message.latitude, lon=event.message.longitude)
        # message=TextSendMessage(text=fiveNear,quick_reply=QuickReply(items=[QuickReplyButton(action=PostbackAction(label="開啟按鈕",data="123"))]))
        message = TextSendMessage(text=fiveNear, quick_reply=QuickReply(
            items=[QuickReplyButton(action=PostbackAction(label=">>資料傳送門請點我<<",
                                data=str({"parkloc":fiveNameAddr,"lat":event.message.latitude,"lon":event.message.longitude}),
                                display_text='可以打開路線規劃搜尋囉~'))]))
        #data = str({'addr': fiveNameAddr, 'usrlat': event.message.latitude, 'usrlon': event.message.longitude})
        #message=TextSendMessage(text="緯度:"+str(event.message.latitude)+"\n"+"經度:"+str(event.message.longitude))
        line_bot_api.reply_message(event.reply_token,message)

        #getParam(nearpark.getNearToGo(cntDistPark))

    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

def sendGoPlan(event,**parkargs):
    try:

        print("eeeee:", event)
        # if(event=='none'):
        #     global usrlat,usrlon
        #     usrlat=parkargs['lat']
        #     usrlon=parkargs['lon']
        #     print("usrlat::",usrlat,"usrlon::",usrlon)
        #     return

        if (event.type == 'postback'):
            global testdata
            testdata = []
            print("testargs:", parkargs)
            test = parkAPI.DealShowInfo(passparg=parkargs['pargs'])
            print("backargs:", test.testrlt())
            testdata.append(test.testrlt())
            print("testdata:", testdata[0])
        elif (event.type == 'message'):
            print("testpasssucc:", testdata[0])
            nearAddr=eval(testdata[0])
            trans=[index for index in nearAddr['parkloc'].keys()]
            print("trans:",trans)
            usrlat = nearAddr.get('lat')
            usrlon = nearAddr.get('lon')
            for i in trans:
                print("name:::",nearAddr.get('parkloc').get(i)[0],"mapurl:::",'https://www.google.com/maps/dir/?api=1&origin={}%2C{}&destination={}%2C{}'.format(usrlat,usrlon,nearAddr.get('parkloc').get(i)[1],nearAddr.get('parkloc').get(i)[2]),"lat:::",nearAddr.get('parkloc').get(i)[1],"lon:::",nearAddr.get('parkloc').get(i)[2])

            print("usrlat::",usrlat,"usrlon::",usrlon)
            #message = TextSendMessage(text=str(testdata[0]))
            message = TemplateSendMessage(
                alt_text='停車場路徑規劃',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            title=nearAddr.get('parkloc').get(trans[0])[0],
                            text=nearAddr.get('parkloc').get(trans[0])[0],
                            actions=[URITemplateAction(label="開啟地圖",
                                uri='https://www.google.com/maps/dir/?api=1&origin={}%2C{}&destination={}%2C{}'.format(usrlat,usrlon,nearAddr.get('parkloc').get(trans[0])[1],nearAddr.get('parkloc').get(trans[0])[2]))]),
                        CarouselColumn(
                            title=nearAddr.get('parkloc').get(trans[1])[0],
                            text=nearAddr.get('parkloc').get(trans[1])[0],
                            actions=[URITemplateAction(label="開啟地圖",
                                uri='https://www.google.com/maps/dir/?api=1&origin={}%2C{}&destination={}%2C{}'.format(usrlat,usrlon,nearAddr.get('parkloc').get(trans[1])[1],nearAddr.get('parkloc').get(trans[1])[2]))]),
                        CarouselColumn(
                            title=nearAddr.get('parkloc').get(trans[2])[0],
                            text=nearAddr.get('parkloc').get(trans[2])[0],
                            actions=[URITemplateAction(label="開啟地圖",
                                uri='https://www.google.com/maps/dir/?api=1&origin={}%2C{}&destination={}%2C{}'.format(usrlat,usrlon,nearAddr.get('parkloc').get(trans[2])[1],nearAddr.get('parkloc').get(trans[2])[2]))]),
                        CarouselColumn(
                            title=nearAddr.get('parkloc').get(trans[3])[0],
                            text=nearAddr.get('parkloc').get(trans[3])[0],
                            actions=[URITemplateAction(label="開啟地圖",
                                uri='https://www.google.com/maps/dir/?api=1&origin={}%2C{}&destination={}%2C{}'.format(usrlat,usrlon,nearAddr.get('parkloc').get(trans[3])[1],nearAddr.get('parkloc').get(trans[3])[2]))]),
                        CarouselColumn(
                            title=nearAddr.get('parkloc').get(trans[4])[0],
                            text=nearAddr.get('parkloc').get(trans[4])[0],
                            actions=[URITemplateAction(label="開啟地圖",
                                uri='https://www.google.com/maps/dir/?api=1&origin={}%2C{}&destination={}%2C{}'.format(usrlat,usrlon,nearAddr.get('parkloc').get(trans[4])[1],nearAddr.get('parkloc').get(trans[4])[2]))])
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        else:
            pass


    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))

# def testparam(event,*parkargs):
#     print("park:",parkargs)
#     parkAPI.DealShowInfo(parkargs)


def setQuery(event):
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='789'))
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
