import reflex as rx
import webenreflex.styles.styles as Styles
from webenreflex.styles.styles import navbar_title_style
from webenreflex.styles.styles import Size as Size
from webenreflex.styles.Colors import Colors as Colors 

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
