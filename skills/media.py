from linebot.models import AudioSendMessage, VideoSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill("{media}")
def get(message_request: MessageRequest):
    audio = AudioSendMessage(
        original_content_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        duration=6000,
    )

    video = VideoSendMessage(
        original_content_url="https://i.imgur.com/n8QsXTk.mp4",
        preview_image_url="https://i.imgur.com/oLvTjtu.png",
    )

    return [audio, video]
