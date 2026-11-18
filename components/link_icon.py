import reflex as rx
import webenreflex.styles.styles as styles
from webenreflex.styles.styles import Size as Size


def link_icon(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=styles.Size.DEFAULT.value,
            
        ),
        href=url,
        is_external=True
    ) 
    
