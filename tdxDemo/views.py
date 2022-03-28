import sys
import json

sys.path.append("C:\\herokuenv\\eHualien")
#print(sys.path)
# Create your views here.
from django.conf import settings
#from eHualien import settings
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import * #MessageEvent, TextMessage,LocationMessage
from tdxDemo import func
from urllib.parse import parse_qsl

#settings.configure(DEBUG=True)
line_bot_api=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser=WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if(request.method=='POST'):
        signature=request.META['HTTP_X_LINE_SIGNATURE']
        body=request.body.decode('utf-8')
        try:
            events=parser.parse(body,signature)
            print(events)

        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:

            if isinstance(event,MessageEvent):
                if isinstance(event.message,TextMessage):
                    mtxt=event.message.text
                    if mtxt=='路況待開發':
                        # func.sendRealTraffic(event)
                        pass
                    elif mtxt=='商家待開發':
                        pass
                    elif mtxt=='我附近的停車場在哪呢?':
                        func.shareUsrLoc(event)
                    elif mtxt=='指引我方向吧!!':
                        func.sendGoPlan(event)
                    elif mtxt=='今天我想查點..':
                        func.setQuery(event)
                    elif mtxt=='還有多少車位呢?':
                        func.sendPark(event)
                    else:
                        pass
                if isinstance(event.message, LocationMessage):
                    func.getNearPark(event)
                #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
            elif isinstance(event,PostbackEvent):
                # usrID=event.source.sender_id
                backdata=dict(parse_qsl(event.postback.data))
                #func.changeMenu(usrID,backdata)
                func.setQuery(event,pargs=event.postback.data)

            else:
                pass
        return HttpResponse()

    else:
        return HttpResponseBadRequest()
