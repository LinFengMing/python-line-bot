from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import CameraAction, CameraRollAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill("{action-camara}")
def get(message_request: MessageRequest):
    camara = TemplateSendMessage(
        alt_text="Actions",
        template=ButtonsTemplate(
            title="Menu",
            text="相片選擇器",
            actions=[CameraAction(label="開啟相機"), CameraRollAction(label="開啟相簿")],
        ),
    )

    return [camara]
