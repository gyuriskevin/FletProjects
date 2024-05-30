import base64
import flet as ft

def main(page: ft.Page):
    page.title = "Képinformációk"
    page.window_width = 400
    page.window_height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ft.Text("Képbeolvasás", size=40, weight="bold"))

    image_holder = ft.Image(visible=False, width=200, height=200, fit=ft.ImageFit.CONTAIN)
    
    kep_container = ft.Container(
        content=image_holder,
        width=220,
        height=220,
        padding=10,
    )
    
    img_info = ft.Text(visible=False, size=15, weight=ft.FontWeight.BOLD)
    
    def handle_loaded_file(e: ft.FilePickerResultEvent):
        if e.files and len(e.files):
            selected_file = e.files[0]
            with open(selected_file.path, "rb") as r:
                image_holder.src_base64 = base64.b64encode(r.read()).decode("utf-8")
                image_holder.visible = True
                img_info.value = f"Fájlnév: {selected_file.name}, Méret: {selected_file.size // 1024} KB"
                img_info.visible = True
                kep_container.border = ft.border.all(2, color=ft.colors.BLACK)
                page.update()
    
    file_picker = ft.FilePicker(on_result=handle_loaded_file)
    page.overlay.append(file_picker)
    
    page.add(ft.ElevatedButton(text="Kép kiválasztása", color=ft.colors.BLUE, on_click=lambda _: file_picker.pick_files(allow_multiple=False, allowed_extensions=["jpg", "png", "jpeg"]))) 
    page.add(kep_container)
    page.add(img_info)
    page.update()

ft.app(target=main)
