import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import  Size as Size
from link_bio.styles.styles import Spacing as Spacing
from link_bio.styles.Colors import Colors as Colors 


def link_botton(title: str, body: str,  url: str,image: str) -> rx.Component:
    return rx.link(
          
        rx.button(
            
            rx.hstack(
                
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=Size.SMALL.value 
                ),
                rx.vstack(
                    rx.text(
                        title, 
                        style=styles.button_title_style,
                        color=Colors.PRYMARY.value,
                        ),
                     
                 
                    rx.text(
                        body,
                        style=styles.button_body_style,
                        color=Colors.SECONDARY.value, 
                        ),
                    spacing=Spacing.SMALL.value,
                    align="start",
                    justify="center",
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
                align="center",  # Esto alinea verticalmente el icono y el vstack de texto
              spacing="4",  # Espacio horizontal entre el icono y el bloque de texto
              width="100%",
            ),
            
           background_color=Colors.CONTENT.value, 
           width="100%", 
        
        ),
        
        href=url,
        is_external=True,
        width="100%",
        
    )
