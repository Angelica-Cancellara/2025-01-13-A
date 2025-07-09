import flet as ft
from UI.view import View
from model.model import Model


class Controller:

    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        #controllo dropdown
        if self._view.dd_localization.value is None:
            self._view.create_alert("Selezionare localization!")
            return
        localization = self._view.dd_localization.value

        #stampa risultati
        self._view.txt_result.controls.clear()
        self._model.creaGrafo(localization)
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {self._model.getNumNodi()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi: {self._model.getNumEdges()}"))

        sorted_edges = self._model.getEdges()
        for edge in sorted_edges:
            self._view.txt_result.controls.append(
                ft.Text(f"{edge[0].GeneID} <-> {edge[1].GeneID}: peso {edge[2]["weight"]}"))

        self._view.update_page()

    def analyze_graph(self, e):
        componenti_connesse = self._model.get_connessa()
        self._view.txt_result.controls.append(ft.Text(f"\nLe componenti connesse sono:"))
        for connessa in componenti_connesse:
            if len(connessa) > 1:
                stringa = ""
                for nodo in connessa:
                    stringa += f"{nodo.GeneID}, "
                stringa += f" | dimensione componente = {len(connessa)}"
                self._view.txt_result.controls.append(ft.Text(stringa))
        self._view.update_page()

    def handle_path(self, e):
        pass

    def fillDDLocalizzazione(self):
        for l in self._model.getLocalizzazione():
            self._view.dd_localization.options.append(ft.dropdown.Option(l))
        self._view.update_page()

