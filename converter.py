import itertools
import os


def g_to_sat(graph, c=3, output="is_3_colorable.cnf"):
    try:
        os.remove(output)
    except OSError:
        pass
    n_nodes = len(graph)
    n_var = c*n_nodes
    formula = ""
    # first color assignments
    for i in range(n_nodes):
        # at least one color assigned
        for j in range(1,c+1):
            formula += str(c*i + j) + " "
        formula += str(0) + "\n"
        # not two colors assigned
        for a,b in list(itertools.combinations(range(i*c +1, (i+1)*c + 1), r=2)):
            formula += str(-a) + " " + str(-b) + " 0\n"
    for i in range(n_nodes):
        id = i * c + 1
        neighbours = graph[i]
        # all edges
        for j in neighbours:
            neighbour_id = j * c +1
            for l in range(c):
                # for each color both nodes can't have the same color
                formula += str(-(id + l)) + " " + str(-(neighbour_id +l)) + " 0\n"
    n_lines = formula.count('\n')
    f = open(output, "a")
    f.write("p cnf " + str(n_var) + " " + str(n_lines)+"\n")
    f.write(formula)
    f.close()
    return formula