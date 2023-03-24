from typing import Hashable
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> int:
    """
    Функция считает число компонент связности графа.

    :param g: Граф NetworkX, по которому нужно посчитать число компонент
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: число компонент связности графа.
    """

    visited = {node: False for node in g.nodes}
    subgraph = 1

    def rec_dfs(current_node):
        visited[current_node] = True
        for neighbor in g.neighbors(current_node):
            if not visited[neighbor]:
                rec_dfs(neighbor)

    rec_dfs(start_node)

    for key, value in visited.items():
        if value is False:
            rec_dfs(key)
            subgraph += 1

    return subgraph


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('B', 'C'),
        ('C', 'D'),
        ('F', 'G')
    ])
    print(dfs(graph, "A"))
