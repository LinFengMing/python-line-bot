from linebot.models import TextSendMessage, ImageSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill("{image}")
def get(message_request: MessageRequest):
    msg = ImageSendMessage(
        original_content_url="https://via.placeholder.com/1024x768/333.png/fff",
        preview_image_url="https://via.placeholder.com/800x600/333.png/fff",
    )
    return [msg]
