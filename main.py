from flet import *
import flet as ft
from flet_core import page
from flet_core.types import MainAxisAlignmentString
import requests
import webbrowser

def open_youtube(ylink):
    url=ylink
    webbrowser.open(url)
    
def main(page: ft.Page):
    page.scroll = "always"
    response = requests.get('https://movie-review-3gg6.onrender.com/api/movies')
    movie_dict=response.json()    
    page.update()
    
    for i in range(0,len(movie_dict)):
        page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Row([ft.Container(content=ft.Image(
                            src=movie_dict[i]["poster"],
                            width=100,
                            height=150,
                            fit=ft.ImageFit.FILL,
                            ),margin=10,
                                padding=10,
                                alignment=ft.alignment.center,
                                 width=100,
                                height=150,
                                border_radius=10,),ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text(movie_dict[i]["title"]),
                            subtitle=ft.Text(movie_dict[i]["genres"]
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Play Trailer",on_click=open_youtube(movie_dict[i]["trailerLink"])), ft.TextButton("Reviews")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ],alignment=ft.CrossAxisAlignment.CENTER,

                ),],
                width=600,
                height=200,
            ),padding=10), 

        )
    )
    page.update()
    

ft.app(target=main)