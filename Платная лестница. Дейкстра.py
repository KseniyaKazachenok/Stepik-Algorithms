from typing import Union

import networkx as nx
from networkx.classes.function import path_weight


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    if graph.number_of_nodes() == 2:
        return graph.edges[0, 1]["weight"]
    if graph.number_of_nodes() == 3:
        return graph.edges[0, 2]["weight"]
    else:
        min_path = nx.shortest_path(graph, 0, (graph.number_of_nodes() - 1), weight="weight")
        min_cost = path_weight(graph, min_path, weight="weight")
        return min_cost
    # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы


def gr(graph, costs):
    for i in range(len(costs)):
        graph.add_weighted_edges_from([
            (i, i + 1, costs[i])
        ])
    for i in range(len(costs) - 1):
        graph.add_weighted_edges_from([
            (i, i + 2, costs[i + 1])
        ])
    return graph


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = nx.DiGraph()
    stairway_graph = gr(stairway_graph, stairway)
    # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней

    print(stairway_path(stairway_graph))  # 72
