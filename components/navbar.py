import reflex as rx
import link_bio.styles.styles as Styles
from link_bio.styles.styles import navbar_title_style
from link_bio.styles.styles import Size as Size
from link_bio.styles.Colors import Colors as Colors 

def navbar()-> rx.Component:
    return rx.hstack(
        
         rx.text(
                "Defoy",
               
                color=Colors.PRYMARY.value,
            ),
            rx.text(
                "System",
                
                color=Colors.SECONDARY.value,
                 
            ),
          style=Styles.navbar_title_style,
        position="sticky",
        bg=Colors.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )