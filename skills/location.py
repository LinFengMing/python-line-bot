from linebot.models import LocationSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill("{location}")
def get(message_request: MessageRequest):
    msg = LocationSendMessage(
        "臺北101", address="信義路", latitude=25.033, longitude=121.564
    )

    return [msg]
