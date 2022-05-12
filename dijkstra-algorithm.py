graph = {
    'start': {
        'a': 6,
        'b': 2,
    },
    'a': {
        'fin': 1,
    },
    'b': {
        'a': 3,
        'fin': 5,
    },
    'fin': {}
}

costs = {
    'a': 6,
    'b': 2,
    'fin': float('inf'),
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

def find_lowest_cost_node(costs={}, processed=[]):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        # 如果当前节点的开销最低，且未处理过，就将其设为当前最低开销节点
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node

# 狄克斯特拉算法，计算正向加权图的最短路径
def dijkstra(graph={}, costs={}, parents={}, processed=[]):
    node = find_lowest_cost_node(costs, processed)

    # 如果还有未处理完的节点
    while node is not None:
        # 获取当前节点的开销
        cost = costs[node]
        # 获取当前节点所有的邻居
        neighbors = graph[node]
            
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # 如果当前路径的开销更低，则更新邻居的开销和父节点
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node

        # 保存已经处理过的节点 
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    
    return [costs, parents]

dijkstra(graph, costs, parents)
