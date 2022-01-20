from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import PostbackAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill("{action-postback}")
def get(message_request: MessageRequest):
    msg = TemplateSendMessage(
        alt_text="Actions",
        template=ButtonsTemplate(
            title="Menu",
            text="Please Click",
            actions=[PostbackAction(label="test", data="1")],
        ),
    )

    return [msg]
