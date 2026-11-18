import reflex as rx 
from link_bio.styles.styles import Size as Size
from link_bio.styles.Colors import Colors as Colors 
from link_bio.styles.Colors import TextColor as TextColor
from link_bio.styles.fonts import FontWeight as FontWeight


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
                title, 
                font_wight="blod",
                
                font_size=Size.VERY_BIG.value,
                color= Colors.PRYMARY.value 
                ),
        rx.text(
                f"{body}", 
                font_wigth="Comic Sans MS",
                font_size=Size.DEFAULT.value,
               color = TextColor.BODY.value,
               
                
            ),
    )
    