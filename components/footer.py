import reflex as rx 
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.Colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="/DefoySystem.ico",
                width="64px",
                height="64px",
            ),
        rx.link(f"© 2016-{datetime.date.today().year} Esto es una prueba de conceptos para pagina web",
                href="https://www.indec.gob.ar", is_external=True,
                font_size=Size.MEDIUM.value,
                margin_top=Size.ZERO.value 
                ),
        rx.text("estamos comenzando",
                font_size=Size.MEDIUM.value),
        align="center",
        margin_bottom=Size.BIG.value,
        padding_y=Size.BIG.value,
        padding_x=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value 
        
    )
