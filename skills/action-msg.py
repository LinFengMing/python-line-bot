from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import MessageAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill("{action-message}")
def get(message_request: MessageRequest):
    msg = TemplateSendMessage(
        alt_text="Actions",
        template=ButtonsTemplate(
            title="Menu",
            text="Please Click",
            actions=[MessageAction(label="點我看貼圖", text="{sticker}")],
        ),
    )

    return [msg]
