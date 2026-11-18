import reflex as rx 
from enum import Enum
from link_bio.styles.Colors import Colors 
from link_bio.styles.Colors import TextColor as TextColor
from link_bio.styles.fonts import  FontWeight as FontWeight
from link_bio.styles.fonts import Font as Font


MAX_WIDTH = "600px"

#Sizes 
STYLESHEETS= [
    "https://fonts.googleapis.com/css2?family=poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=confortaa:wght@500&display=swap",
    
    ]

class Size(Enum):
    ZERO = "0px  !important"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "4em"
    VERY_BIG = "9em"
#styles
BASE_STYLE = {
    "font_family":Font.DEFAULT.value,
    "font_Weight":FontWeight.LIGHT,
    "background_color": Colors.BACKGROUND.value,  
    rx.heading: {
        "size": '4',
        "color": TextColor.HEADER.value,   
        "font_family":Font.TITLE.value,
        "font_Weight":FontWeight.MEDIUM,
    },
    rx.button: {
        "width" : "100%",
        "height": "100%",
        
        "padding": Size.SMALL.value,
        #"border_radius": Size.DEFAULT,
        "color": TextColor.HEADER.value,
        "background_color": Colors.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        
        "_hover":{ 
            "background_color": Colors.SECONDARY.value,
            
            
        }
    },
    
    rx.link: {
        "text_decoration":"none",
        "_hover": {} 
        
    }
    
}
navbar_title_style = dict(
         font_family=Font.LOGO.value,
         font_size=Size.LARGE.value,
         font_Weight=FontWeight.MEDIUM,
)
title_style = dict(
            width= "100%",
           
            
            padding_top=Size.DEFAULT.value, 
           
)


button_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    font_Weight=FontWeight.MEDIUM,
    
)
button_body_style = dict(
    font_Weight=FontWeight.LIGHT,
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
    
)

class Spacing(Enum):
    SMALL = "2"
    MEDIUM = "4"
    LARGE = "6"
    BIG = "9"
    VERY_BIG = "12"
    

