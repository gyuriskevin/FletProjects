import flet as ft
import time
import random

def main(page: ft.Page):
    page.title = "Quiz App"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 800
    page.window_resizable = False

    correct_answers = 0
    current_question = 0

    def check_answer(e):
        nonlocal correct_answers
        if e.control.data == "correct":
            e.control.bgcolor = ft.colors.GREEN_200
            correct_answers += 1
        else:
            e.control.bgcolor = ft.colors.RED_200
        e.control.update()
        page.update()
        time.sleep(2)
        show_next_question()

    def show_next_question():
        nonlocal current_question
        current_question += 1
        if current_question < len(questions):
            question_view.controls[0].value = questions[current_question]["question"]
            answers = questions[current_question]["answers"]
            random.shuffle(answers)  # Shuffle the answers
            answers_view.controls.clear()
            for answer in answers:
                answers_view.controls.append(
                    ft.ElevatedButton(
                        content=ft.Text(answer["text"]),
                        data=answer["correct"],
                        on_click=check_answer,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10))
                        ),
                        width=170,
                        height=30,
                    )
                )
            page.update()
        else:
            question_view.controls[0].value = f"Quiz completed! You got {correct_answers} out of {len(questions)} questions right."
            answers_view.controls.clear()
            page.update()


    questions = [
        {
            "question": "What is the capital of France?",
            "answers": [
                {"text": "Paris", "correct": "correct"},
                {"text": "London", "correct": "incorrect"},
                {"text": "Berlin", "correct": "incorrect"},
                {"text": "Madrid", "correct": "incorrect"},
            ],
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "answers": [
                {"text": "Mars", "correct": "correct"},
                {"text": "Jupiter", "correct": "incorrect"},
                {"text": "Saturn", "correct": "incorrect"},
                {"text": "Venus", "correct": "incorrect"},
            ],
        },
        {
            "question": "Who painted the Mona Lisa?",
            "answers": [
                {"text": "Leonardo da Vinci", "correct": "correct"},
                {"text": "Vincent van Gogh", "correct": "incorrect"},
                {"text": "Pablo Picasso", "correct": "incorrect"},
                {"text": "Michelangelo", "correct": "incorrect"},
            ],
        },
        {
            "question": "What is the largest ocean in the world?",
            "answers": [
                {"text": "Pacific Ocean", "correct": "correct"},
                {"text": "Atlantic Ocean", "correct": "incorrect"},
                {"text": "Indian Ocean", "correct": "incorrect"},
                {"text": "Arctic Ocean", "correct": "incorrect"},
            ],
        },
        {
            "question": "Which country is known for inventing pizza?",
            "answers": [
                {"text": "Italy", "correct": "correct"},
                {"text": "Greece", "correct": "incorrect"},
                {"text": "Spain", "correct": "incorrect"},
                {"text": "France", "correct": "incorrect"},
            ],
        },
        {
            "question": "Who wrote the play Romeo and Juliet?",
            "answers": [
                {"text": "Shakespeare", "correct": "correct"},
                {"text": "Wilde", "correct": "incorrect"},
                {"text": "Shaw", "correct": "incorrect"},
                {"text": "Williams", "correct": "incorrect"},
            ],
        },
        {
            "question": "Which two countries share the longest international border?",
            "answers": [
                {"text": "Canada", "correct": "correct"},
                {"text": "United States", "correct": "correct"},
                {"text": "China", "correct": "incorrect"},
                {"text": "Russia", "correct": "incorrect"},
            ],
        },
        {
            "question": "Which two colors are on the flag of Ukraine?",
            "answers": [
                {"text": "Blue", "correct": "correct"},
                {"text": "Yellow", "correct": "correct"},
                {"text": "Red", "correct": "incorrect"},
                {"text": "Green", "correct": "incorrect"},
            ],
        },
        {
            "question": "Which two colors are on the flag of Ukraine?",
            "answers": [
                {"text": "Blue", "correct": "correct"},
                {"text": "Yellow", "correct": "correct"},
                {"text": "Red", "correct": "incorrect"},
                {"text": "Green", "correct": "incorrect"},
            ],
        },
    ]

    def start_quiz(e):
        landing_view.visible = False
        quiz_view.visible = True
        show_next_question()
        page.update()

    landing_view = ft.Column(
        controls=[
            ft.Text("Welcome to the Quiz App!", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(
                "Test your knowledge with this fun quiz! You will be presented with a series of questions. "
                "Choose the correct answer(s) for each question. At the end, you will see your score.",
                size=16,
                text_align=ft.TextAlign.JUSTIFY,
            ),
            ft.ElevatedButton("Start Quiz", on_click=start_quiz),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    question_view = ft.Column(
        controls=[
            ft.Text(
                "",
                size=20,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    answers_view = ft.Row(
        wrap=True,
        spacing=10,
        run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    quiz_view = ft.Column(
        visible=False,
        controls=[
            question_view,
            answers_view,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    )

    page.add(
        ft.Column(
            controls=[
                landing_view,
                quiz_view,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

ft.app(target=main)
