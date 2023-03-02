
def create_clique(n):
    graph = []
    for i in range(n):
        neighbours = []
        for j in range(n):
            if i != j:
                neighbours.append(j)
        graph.append(neighbours)
    return graph


def create_cycle(n):
    graph = [[n - 1, 1]]
    for i in range(1,n-1):
        graph.append([i-1, i+1])
    graph.append([n-2, 0])
    return graph


def create_grid(n, m):
    graph = []
    for i in range(n*m):
        id = i
        row = int(i/m)
        top = id-m
        bottom = id+m
        left = id-1
        right = id+1
        neighbours = []
        if top >= 0:
            neighbours.append(top)
        if left >= row*m:
            neighbours.append(left)
        if right < (row+1)*m:
            neighbours.append(right)
        if bottom < n*m:
            neighbours.append(bottom)
        graph.append(neighbours)
    return graph


def create_torus(n, m):
    graph = []
    for i in range(n*m):
        id = i
        row = int(i/m)
        column = id - row * m
        top = id-m
        if row == 0:  # first row wrap around top
            top = (n-1)*m + id
        bottom = id+m
        if row == n-1:  # last row wrap around bottom
            bottom = id % m
        left = id-1
        if column == 0:  # first column wrap around left
            left = row * m + (m-1)  # last element in current row
        right = id+1
        if column == m-1:  # last column wrap around right
            right = row * m
        neighbours = [top,left,right,bottom]
        graph.append(neighbours)

    return graph


def create_klein_bottle(n, m):
    graph = []
    for id in range(n*m):
        row = int(id/m)
        column = id - row * m
        top = id-m
        if row == 0:  # first row wrap around top same as torus
            top = (n-1)*m + id
        bottom = id+m
        if row == n-1:  # last row wrap around bottom same as torus
            bottom = id % m
        left = id-1
        if column == 0:  # first column wrap around left antipolar
            left = (n-1-row) * m + (m-1)  # last element in antipolar row
        right = id+1
        if column == m-1:  # last column wrap around right
            right = (n-1-row) * m  # first element in antipolar row
        neighbours = [top,left,right,bottom]
        graph.append(neighbours)
    return graph


def create_gadget(k):
    graph = []
    for id in range(k*k):
        row = int(id / k)
        column = id - row * k
        neighbours = []
        for i in range(k*k):
            row_i = int(i / k)
            column_i = i - row_i * k
            if row_i != row and column_i != column:
                neighbours.append(i)
        graph.append(neighbours)
    return graph


def create_gadget_cycle(k, l):
    graph = []
    for j in range(l):
        offset = j * k*k
        # creating the next gadget
        for id in range(offset, offset + k*k):
            local_id = id % (k*k)
            row = int(local_id / k)
            column = local_id - row * k
            neighbours = []
            for i in range(offset, offset + k*k):
                local_i = i % (k * k)
                row_i = int(local_i / k)
                column_i = local_i - row_i * k
                if row_i != row and column_i != column:
                    neighbours.append(i)
            graph.append(neighbours)
    # connecting the two gadgets from newly created backwards
    connect_gadgets(graph, k, l-1, 0)
    for i in range(0,l-1):
        connect_gadgets(graph, k, i, i+1)
    return graph


# connects kxk gadgets nr1 and nr2 by having a 90 degree right twist connection from nr1 to nr 2
def connect_gadgets(graph, k, nr1, nr2):
    offset_nr1 = nr1 * k*k
    offset_nr2 = nr2 * k*k
    for i_1 in range(offset_nr1, offset_nr1 + k * k):
        local_id_1 = i_1 % (k * k)
        row_1 = int(local_id_1 / k)
        column_1 = local_id_1 - row_1 * k
        # twist 90 degree right
        t_row = column_1
        t_column = k - 1 - row_1
        new_neighbours = []
        for i_2 in range(offset_nr2, offset_nr2 + k * k):
            local_id_2 = i_2 % (k * k)
            row_i = int(local_id_2 / k)
            column_i = local_id_2 - row_i * k
            if row_i != t_row and column_i != t_column:
                new_neighbours.append(i_2)
        graph[i_1].extend(new_neighbours)

if __name__ == "__main__":
    print(create_gadget_cycle(3, 2))