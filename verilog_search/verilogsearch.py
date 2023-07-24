import math
from queue import Queue

import networkx as nx
import numpy


class VerilogSearch:
    def __init__(self, module_graph: nx.DiGraph):
        """
        Constructor for Verilog Search class
        :param module_graph: Graph representation as nx object
        """
        self.__module_graph = module_graph

    def get_longest_path(self):
        """
        Apply BFS to find the longest path in graph
        :return: the longest value
        """
        # Get adjacency lists
        vertices: numpy.ndarray = nx.adjacency_matrix(self.__module_graph)
        queue = Queue()

        # apply BFS
        graph_size: int = int(math.sqrt(vertices.size))
        used = {0: 1}
        queue.put(0)
        while not queue.empty():
            node = queue.get()
            for i in range(0, graph_size):
                if i not in used:
                    used[i] = used[node] + 1
                    queue.put(i)

        # get max length
        return max(used.values())


