import reflex as rx 
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.views.sponsors.sponsor import sponsor 
from link_bio.styles.styles import Size as Size
from link_bio.styles.fonts import Font as  Font

class State(rx.State):
    
    pass

def index () -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
              
                links(),
                max_width=styles.MAX_WIDTH,
                align="center",
                spacing="5",
                justify="start",
                width="100%",
                min_height="100vh",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                
              
                    ),
            
            ),
        sponsor(),
        footer()
    )
    
       
    
    

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index,
             title="Defoy System",
             description="Enlaces de contacto y redes sociales de Alfredo Defoy",
             image="avatar1.jpg",)

