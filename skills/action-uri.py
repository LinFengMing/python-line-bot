from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill("{action-uri}")
def get(message_request: MessageRequest):
    msg = TemplateSendMessage(
        alt_text="Actions",
        template=ButtonsTemplate(
            title="Menu",
            text="Please Click",
            actions=[
                URIAction(
                    label="google",
                    uri="https://www.google.com.tw?openExternalBrowser=1",
                )
            ],
        ),
    )

    return [msg]
