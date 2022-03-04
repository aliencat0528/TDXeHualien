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
                    if mtxt=='搜搜停車場':
                        func.sendPark(event)
                    elif mtxt=='看看即時路況':
                        func.sendRealTraffic(event)
                    elif mtxt=='查查路線規劃':
                        func.sendGoPlan(event)
                    else:
                        pass
                if isinstance(event.message, LocationMessage):
                    func.getUsrLoc(event)
                #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

        return HttpResponse()

    else:
        return HttpResponseBadRequest()
def showDB():
    pass
