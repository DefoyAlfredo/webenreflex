import reflex as rx 
from webenreflex.styles.styles import Size as Size
from webenreflex.styles.Colors import Colors as Colors 
from webenreflex.styles.Colors import TextColor as TextColor
from webenreflex.styles.fonts import FontWeight as FontWeight


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
    
