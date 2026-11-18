import reflex as rx 
from webenreflex.components.navbar import navbar
from webenreflex.views.header.header import header
from webenreflex.views.links.links import links
from webenreflex.components.footer import footer
import webenreflex.styles.styles as styles
from webenreflex.views.sponsors.sponsor import sponsor 
from webenreflex.styles.styles import Size as Size
from webenreflex.styles.fonts import Font as  Font

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

