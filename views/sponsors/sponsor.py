import reflex as rx
from webenreflex.styles.styles import Size as Size
from webenreflex.components.title import title
from webenreflex.components.link_sponsor import link_sponsor
from webenreflex.styles.styles import Size


def sponsor() -> rx.Component:
    return rx.vstack(
        rx.center(
            title("Colaboran"),
        ),
    
        rx.hstack(
            
            link_sponsor(
                "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Logo_Universitat_de_Valencia.svg/2560px-Logo_Universitat_de_Valencia.svg.png",
                "https://www.uv.es/",
            ),
            link_sponsor(
                "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Logo_Universitat_de_Valencia.svg/2560px-Logo_Universitat_de_Valencia.svg.png",
                "https://www.uv.es/uvweb/universidad/es/estudios-grado-1285846070123.html",
            ),
             
        ),
        Spacing=Size.BIG.value, 
        width="100%",
    align_items="center",
   
    )
