import reflex as rx
from reflex import assets
from webenreflex.components.link_botton import link_botton
from webenreflex.components.title import title
from webenreflex.styles.styles import Size as Size
from webenreflex.styles.styles import Spacing
from webenreflex.styles.Colors import TextColor as TextColor
from webenreflex.styles.Colors import Colors as Colors 
 

#
def links() -> rx.Component:
    return rx.vstack(
        title("COMUNIDAD"),
        link_botton("Twitch",
                    "pruebas ", 
                    "https://twitch.tv",
                    "icons/twitch-brands-solid-full.svg"
                    ),
        link_botton("Yuotube",
                    "Canal",
                    "https://www.youtube.com/@DefoySystem",
                    "icons/youtube-brands-solid-full.svg"
                    
                    ),
        link_botton("Discord",
                    "chat de comunidad de pruebas",
                    "https://discord.com/users/804827724568461335",
                    "icons/discord-brands-solid.svg"
                    ),
                    
        
        title("CONTACTO"),
                link_botton("GIT:",
                            "Mis Proyectos ", 
                            "https://github.com/DefoyAlfredo?tab=repositories",
                            "icons/git-brands-solid.svg",
                            ),
                link_botton("Email:",
                           "alfredodefoy@gmail.com",
                           "mailto:alfredodefoy@gmail.com",
                           "icons/envelope-solid.svg",
                           ),
        width= "100%",
        spacing=Spacing.MEDIUM.value,
        aling="start",
       padding_left=Size.SMALL.value,
        
        
    
    
       
    )
     
