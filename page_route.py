import flet as ft

page = ft.Page()

def route_change(route):
    page.controls.pop()
    if route.route == "/":
        page.add(home_page())
    elif route.route == "/about":
        page.add(about_page())
    page.update()

page.on_route_change = route_change

def home_page():
    return ft.Text("This is the home page")

def about_page():
    return ft.Text("This is the about page")

home_button = ft.Button(text="Home", on_click=lambda _: page.go("/"))
about_button = ft.Button(text="About", on_click=lambda _: page.go("/about"))

page.add(ft.Column([home_button, about_button]))

page.go("/")  

ft.app(target=page) 