from idna import package_data
from linebot.models import StickerSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill("{sticker}")
def get(message_request: MessageRequest):
    sticker = StickerSendMessage(package_id=789, sticker_id=10855)

    return [sticker]
