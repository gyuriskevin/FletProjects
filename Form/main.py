import flet as ft
import time

checked = []
name = {'first_name': '', 'last_name': ''}
pet = False 

def ContainerStyling(header):
    return {
        "height": 130,
        "width": 800,
        "border_radius": 10,
        "border": ft.border.only(top=ft.border.BorderSide(6, "#3F84E5")) if header == "header" else ft.border.only(left=ft.border.BorderSide(6, "#E2DBCB")),
        "bgcolor": "#E2DBCB",
        "animate": ft.animation.Animation(800, "ease"),
        "on_hover": lambda e: onHover(e) if header == "header" else onHoverQ(e),
        "margin": 10,
        "padding" : 10
    }

def onHover(e):
    e.control.height = 140 if e.data == "true" else 130
    e.control.border = ft.border.only(top=ft.border.BorderSide(6, "#3F84E5"))
    e.control.update()

def onHoverQ(e):
    e.control.height = 145 if e.data == "true" else 130
    e.control.border = ft.border.only(left=ft.border.BorderSide(6, "#3F84E5")) if e.data == "true" else ft.border.only(top=ft.border.BorderSide(6, "#E2DBCB"))
    e.control.update()

def getChanges(e):
    global entName
    entName = False
    allowed_chars = "qwertzuiopőúüóöasdfghjkléáűmnbvcxyí "
    if all(char.lower() in allowed_chars for char in e.control.value):
        e.control.error_text = ""
    else:
        e.control.error_text = "Only letters are allowed"
    e.control.update()
    if e.control.label == "First Name":
        name['first_name'] = e.control.value
    elif e.control.label == "Last Name":
        name['last_name'] = e.control.value
    if(len(name['first_name']) > 0 and len(name['last_name']) > 0):
        entName = True
    else:
        entName = False
    checkSubmitAvailability()
    colors.update()

def checkBoxChange(e):
    global checked
    global pet
    if e.control.value:
        checked.append(e.control.label)
    else:
        checked = [label for label in checked if label != e.control.label]
    
    if(len(checked) > 0):
        pet = True
    else:
        pet = False
    
    checkSubmitAvailability()
    colors.update()

def checkSubmitAvailability():
    global pet, entName
    if not (pet and entName and radio.value and (colors.value is not None and len(colors.value) > 0)):
        submit_button.disabled = True
    else:
        submit_button.disabled = False
    submit_button.update()



def main(page: ft.Page):
    page.title = "Form"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#D4CBB3"
    page.scroll = "auto"

    header_content = ft.Row(
        [
            ft.Column([
                ft.Text(
                    value="Form Projekt",
                    size=60,
                    color="#1f1e1e",
                    weight="bold",
                ),
            ]),
        ],
        alignment="center"
    )

    header = ft.Container(**ContainerStyling("header"), content=header_content)

    contentTexts = ["Please enter your information:", "On a scale of 1-5, how would you rate your day?", "What kind of pets do you have at home?", "Choose one color:"]

    first_content = ft.Column(
        [
            ft.Text(
                value=contentTexts[0],
                size=20,
                color="#1f1e1e",
                weight="bold",
            ),
            ft.Row(
                [
                    ft.TextField(
                        label="First Name",
                        width=300,
                        hint_text="Enter your first name",
                        on_change=lambda e: getChanges(e),
                        height=100
                    ),
                    ft.TextField(
                        label="Last Name",
                        width=300,
                        hint_text="Enter your last name",
                        on_change=lambda e: getChanges(e),
                        height=100
                    )
                ],
                alignment="center"
            )
        ],
        alignment="center"
    )

    questions1 = ft.Container(**ContainerStyling("questions"), content=first_content)

    global radio
    radio = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="1", label="1"),
                ft.Radio(value="2", label="2"),
                ft.Radio(value="3", label="3"),
                ft.Radio(value="4", label="4"),
                ft.Radio(value="5", label="5"),
            ],
            alignment="center"
        )
    )
    second_content = ft.Column(
        [
            ft.Text(
                value=contentTexts[1],
                size=20,
                color="#1f1e1e",
                weight="bold",
            ),
            radio
        ],
        alignment="center"
    )

    questions2 = ft.Container(**ContainerStyling("questions"), content=second_content)

    third_content = ft.Column(
        [
            ft.Text(
                value=contentTexts[2],
                size=20,
                color="#1f1e1e",
                weight="bold",
            ),
            ft.Row(
                [
                    ft.Checkbox(label="Dog", on_change=lambda e: checkBoxChange(e)),
                    ft.Checkbox(label="Cat", on_change=lambda e: checkBoxChange(e)),
                    ft.Checkbox(label="Bird", on_change=lambda e: checkBoxChange(e)),
                    ft.Checkbox(label="Fish", on_change=lambda e: checkBoxChange(e)),
                    ft.Checkbox(label="Turtle", on_change=lambda e: checkBoxChange(e)),
                ],
                alignment="center"
            )
        ],
        alignment="center"
    )

    questions3 = ft.Container(**ContainerStyling("questions"), content=third_content)

    global colors
    colors = ft.Dropdown(
        label="Color",
        on_change=lambda e: checkSubmitAvailability(),
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Blue"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Yellow"),
            ft.dropdown.Option("Pink"),
            ft.dropdown.Option("Purple"),
        ]
    )

    fourth_content = ft.Column(
        [
            ft.Text(
                value=contentTexts[3],
                size=20,
                color="#1f1e1e",
                weight="bold",
            ),
            ft.Row(
                [
                    colors
                ],
                alignment="center"
            )

        ],
        alignment="center"
    )

    questions4 = ft.Container(**ContainerStyling("questions"), content=fourth_content)

    global submit_button
    submit_button = ft.ElevatedButton(
        text="Submit",
        on_click=lambda e: submit(e),
        width=100,
        height=30,
        disabled=True 
    )

    global result_text
    result_text = ft.Text(
        value="",
        size=20,
        weight = "bold"
    )

    page.add(header, questions1, questions2, questions3, questions4, submit_button, result_text)

    def submit(e):
        result_text.value = ""
        appendres = ""
        for i in checked:
            appendres += i + " "
        typed_text = f"Name: {name['first_name']} {name['last_name']}\n"
        typed_text += f"Rated your day: {radio.value}\n"
        typed_text += f"Pets: {appendres}\n"
        typed_text += f"Selected color: {colors.value}\n"
        print(typed_text)
        typing = 0.05

        for char in typed_text:
            result_text.value += char
            page.update()
            time.sleep(typing)

    page.update()

ft.app(target=main)
