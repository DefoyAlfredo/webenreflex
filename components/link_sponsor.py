import reflex as rx

from webenreflex.styles.styles import Size


def link_sponsor(imagen: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height=Size.VERY_BIG.value,
            width="auto",
            border_radius=Size.BIG.value
        ),
        href=url,
        is_external=True,
    )
