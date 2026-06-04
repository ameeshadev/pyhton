def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)

    matrix = [[0] * n for _ in range(n)]

    for node in range(n):
        for neighbor in adj_list[node]:
            matrix[node][neighbor] = 1

    for row in matrix:
        print(row)

    return matrix
