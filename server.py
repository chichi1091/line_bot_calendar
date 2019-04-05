import os
import logging

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException, BadRequest, Forbidden

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


LINE_ACCESS_TOKEN = os.environ['LINE_ACCESS_TOKEN']
LINE_CHANNEL_SECRET = os.environ['LINE_CHANNEL_SECRET']
line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route('/line_bot_gmail', methods=['POST'])
def service(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']

        try:
            handler.handle(request.body.decode('utf-8'), signature)
        except InvalidSignatureError:
            return Forbidden()
        except LineBotApiError:
            return BadRequest()

        return HTTPException()
    else:
        return BadRequest()


@handler.default()
def default(event):
    logger.info(event)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='サポートされていないテキストメッセージです')
    )


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    logger.info(event)

    if event.message.text.find('予定') >= 0 or event.message.text.find('スケジュール') >= 0:

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )


if __name__ == '__main__':
    app.run()
