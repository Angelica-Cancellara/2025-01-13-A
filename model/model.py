import copy
import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._edges = []
        self._idMap = {}

    def getLocalizzazione(self):
        return DAO.getLocalizzazione()

    def creaGrafo(self, localization):
        self._graph.clear()
        self._nodes = DAO.getNodi(localization)
        self._graph.add_nodes_from(self._nodes)

        self._idMap = {}
        for n in self._nodes:
            self._idMap[n.GeneID] = n

        self._edges = DAO.getArchi(localization, self._idMap)
        for a in self._edges:
            self._graph.add_edge(a[0], a[1], weight=a[2])

    def getNumNodi(self):
        return self._graph.number_of_nodes()

    def getEdges(self):
        return self._edges

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def get_num_connesse(self):
        return nx.number_connected_components(self._graph)

    def get_connessa(self):
        connesse = list(nx.connected_components(self._graph))
        connesse.sort(key=lambda x: len(x), reverse=True)
        return connesse