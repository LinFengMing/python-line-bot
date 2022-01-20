import os
import re
from pathlib import Path
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from fastapi.params import Header
from starlette.requests import Request
from models.message_request import MessageRequest
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    FollowEvent,
    UnfollowEvent,
    MessageEvent,
    PostbackEvent,
    TextMessage,
    TextSendMessage,
    ImageMessage,
    LocationMessage,
)
from skills import *
from skills import skills

app = FastAPI()

load_dotenv()

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))


def get_message(request: MessageRequest):
    for pattern, skill in skills.items():
        if re.match(pattern, request.intent):
            return skill(request)
    request.intent = "{not_match}"
    return skills["{not_match}"](request)


@app.post("/api/line")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(
            status_code=400,
            detail="Invalid signature. Please check your channel access token/channel secret.",
        )
    return "OK"


@handler.add(event=FollowEvent)
def handle_message(event):
    print("follow", event)

    # 取得使用者個人資訊
    profile = line_bot_api.get_profile(event.source.user_id)
    print(profile.display_name)
    print(profile.user_id)
    print(profile.picture_url)
    print(profile.status_message)

    # 回傳歡迎訊息
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(f"Hi, {profile.display_name}")
    )


@handler.add(event=UnfollowEvent)
def handle_message(event):
    print("unfollow", event)


@handler.add(event=MessageEvent, message=TextMessage)
def handle_message(event):
    msg_request = MessageRequest()
    msg_request.intent = event.message.text
    msg_request.message = event.message.text
    msg_request.user_id = event.source.user_id

    func = get_message(msg_request)
    line_bot_api.reply_message(event.reply_token, func)


@handler.add(event=MessageEvent, message=ImageMessage)
def handle_message(event):
    print("image", event)
    # 取得訊息ID
    message_id = event.message.id
    # 透過訊息ID取得LINE Server上面的檔案
    message_content = line_bot_api.get_message_content(message_id)
    # 將圖片存到伺服器
    with open(Path(f"images/{message_id}.jpg").absolute(), "wb") as f:
        for chunk in message_content.iter_content():
            f.write(chunk)


@handler.add(event=MessageEvent, message=LocationMessage)
def handle_message(event):
    print("location", event)
    print("-----")
    print(event.message.latitude)
    print(event.message.longitude)


@handler.add(event=PostbackEvent)
def handle_message(event):
    print("postback", event.postback)
    print("-----")
    print("params", event.postback.params)
    print("data", event.postback.data)
