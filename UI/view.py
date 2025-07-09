import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "TdP 2024 - Esame del 13/01/2025 - A"
        self._page.horizontal_alignment = 'CENTER'
        self._page.window_width = 800
        self._page.window_height = 800
        self._page.window_center()
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # title
        self._title = None
        # first row
        self.dd_localization: ft.Dropdown = None
        self.btn_graph: ft.ElevatedButton = None
        self.btn_analizza_grafo: ft.ElevatedButton = None
        self.btn_path: ft.ElevatedButton = None
        # second row
        self.txt_result: ft.ListView = None  # Qui scrivere gli outputs


    def load_interface(self):
        # title
        self._title = ft.Text("TdP 2024 - Esame del 13-01-2025 - A", color="blue", size=24)
        self._page.controls.append(self._title)

        # First row with some controls
        self.dd_localization = ft.Dropdown(label="Localization",
                               hint_text="Selezionare un tipo di localization.", width=300)
        self._controller.fillDDLocalizzazione()

        self.btn_graph = ft.ElevatedButton(text="Crea Grafo",
                                           tooltip="Crea il grafo",
                                           on_click=self._controller.handle_graph)

        self.btn_analizza_grafo = ft.ElevatedButton(text="Analizza Grafo",
                                           tooltip="Analizza il grafo",
                                           on_click=self._controller.analyze_graph)

        self.btn_path = ft.ElevatedButton(text="Cammino",
                                          tooltip="Trova cammino ottimo",
                                          on_click=self._controller.handle_path)

        row1 = ft.Row([self.dd_localization, self.btn_graph, self.btn_analizza_grafo, self.btn_path],
                      alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        self._page.controls.append(row1)

        # List View where the reply is printed
        self.txt_result = ft.ListView(width=700, expand=1, spacing=10, padding=20, auto_scroll=False)
        self.txt_result.controls.append(ft.Text("Risultati"))

        container1 = ft.Container(
            content=self.txt_result,
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.GREY_200,
            width=750,
            height=630,
            border_radius=10,
        )
        row2 = ft.Row([container1],
                      alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                      spacing=50)
        self._page.controls.append(row2)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
