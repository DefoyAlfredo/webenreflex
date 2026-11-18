import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.title import title 
from link_bio.styles.styles import Size as Size
from link_bio.styles.styles import Spacing as Spacing 
from link_bio.styles.fonts import Font as  Font
from link_bio.styles.Colors import Colors as Colors 
from link_bio.styles.Colors import TextColor as TextColor




def header() -> rx.Component:
        return rx.vstack(
                
                rx.hstack(
                        rx.box(
                        rx.avatar(
                                src="/avatar1.jpg",
                                size="9", 
                                #radius="medium",
                                color= TextColor.BODY.value,
                                #bg=Colors.CONTENT.value,
                                #padding="4px",
                                #border="10px",
                                #border_color= Colors.PRYMARY.value,
                                border=f"5px solid {Colors.PRYMARY.value}",
                                #border_radius="9999px",
                                padding="2px",
                                
                                ),
                                
                                
                        rx.heading(
                                
                                "Defoy Alfredo",
                                font_size=Size.DEFAULT.value,
                                font_family=Font.DEFAULT.value,
                                
                                color=Colors.PRYMARY.value,
                                margin_top=Size.ZERO.value,
                                
                                          
                                
                        ),
                        
                      
                       
                        rx.text(
                                "@Defoysystem",
                                font_size=Size.MEDIUM.value,
                                margin_top=Size.ZERO.value,
                                color=TextColor.BODY.value
                                
                                ),
                        
                        rx.hstack(
                        
                        link_icon(
                                "icons/youtube-brands-solid-full.svg",
                                "https://www.youtube.com/@DefoySystem",
                                   
                                   
                                   ), 
                             
                        
                        ),
                       
                        align_items="center",
                        spacing=Spacing.SMALL.value ,
                        
                        
                ),
                spacing=Spacing.MEDIUM.value,
                align="end",
                
                
                ),
                
        rx.flex(
         rx.text(
        "+13 ",
        "años de experiencia en mantenimiento de sistemas y pruebas de concepto prácticas",
       font_size=Size.LARGE.value,  
       color=TextColor.BODY.value,
       
    ),
    rx.text(
            f"Realizando conceptos de pruebas en la preparacion de la mi web en reflex",
            font_size=Size.LARGE.value,
            color=TextColor.BODY.value,
            
            ),
   
    
    
    width="100%",
    spacing=Spacing.MEDIUM.value
),
     
    
    
    
    
    
                
                rx.heading("Hola 👋 Soy Alfredo  crando mi web en reflex", size="4"),
                rx.text("Hola es mi primer web"),
                rx.text("Es la primera web hecha en reflex"),
                align="start",
              
                width="100%",
                spacing=Spacing.BIG.value,
                
        )

