# flask、diango架設伺服器或是寫網站
# flask較小 沒有畫面

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#取得權杖，fb twitter都有
line_bot_api = LineBotApi('YYisLs65zvNFHvE98DVMPEBgY7UCGIjkzUfa1+nP8x3u3A5x8UOCyaG0LKgYn7LQy6wkyr2hOWL2pgvgpXIvWIb2xYvUgbrgmGmV5656BHI2kjOMQWI8SwsWS3LI6aq2+av+D0P9PrZucytvOP+YCAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c96360f9d803f6f159b52b60e7548940')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我只是一個機器人，只會回復特定訊息....'

    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了嗎?'
        r = '我吃電，不吃飯...'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()