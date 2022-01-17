from linebot.models import TemplateSendMessage
from linebot.models.template import ImageCarouselTemplate, ImageCarouselColumn
from linebot.models.actions import PostbackAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill("{image_carousel}")
def get(message_request: MessageRequest):
    image_carousel_template_message = TemplateSendMessage(
        alt_text="ImageCarousel template",
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://via.placeholder.com/300x300/333.png/fff",
                    action=PostbackAction(
                        label="postback1",
                        display_text="postback text1",
                        data="action=buy&itemid=1",
                    ),
                ),
                ImageCarouselColumn(
                    image_url="https://via.placeholder.com/300x300/333.png/fff",
                    action=PostbackAction(
                        label="postback2",
                        display_text="postback text2",
                        data="action=buy&itemid=2",
                    ),
                ),
            ]
        ),
    )

    return [image_carousel_template_message]
