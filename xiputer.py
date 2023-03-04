import converter
import generator
import os
import subprocess

solver_command = "kissat"
solver_flags = "-q"
unsat_parse_string = "UNSATISFIABLE"
sat_parse_string = "SATISFIABLE"


def compute_chromatic_number(graph, start=2, filename="colorability_test.cnf", verbose=True):
    colorable = False
    c = start - 1
    while not colorable:
        c += 1
        colorable = convert_and_test_colorability(graph, c, filename, verbose)
    print('chromatic number is ' + str(c))


def compute_chromatic_number_downward(graph, start=20, filename="colorability_test.cnf", verbose=True):
    colorable = True
    c = start + 1
    while colorable:
        c -= 1
        colorable = convert_and_test_colorability(graph, c, filename, verbose)
    print('chromatic number is ' + str(c+1))


def convert_and_test_colorability(graph, c, filename="colorability_test.cnf", verbose=True):
    converter.g_to_sat(graph, c, output=filename)
    result = test_colorability(filename, c, verbose)
    try:
        os.remove(filename)
    except OSError:
        pass
    return result


def test_colorability(cnf_file_path, c, verbose=True):
    result = subprocess.run([solver_command, solver_flags, cnf_file_path], stdout=subprocess.PIPE)
    parsed_output = False
    output = str(result.stdout)
    if sat_parse_string in output:
        colorable = True
        parsed_output = True
    if unsat_parse_string in output:
        colorable = False
        parsed_output = True
    if not parsed_output:
        print("couldn't parse solver output")
        raise IOError
    if verbose and colorable:
        print('is ' + str(c) + ' colorable')
    if verbose and not colorable:
        print('is not ' + str(c) + ' colorable')
    return colorable


def test_clique():
    n = 5
    output = "is_K" + str(n) + "_colorable.cnf"
    graph = generator.create_clique(n)
    compute_chromatic_number(graph, filename=output)


def test_cycle():
    n = 17
    output = "is_Cycle" + str(n) + "_colorable.cnf"
    graph = generator.create_cycle(n)
    compute_chromatic_number(graph, filename=output)


def test_grid():
    n = 17
    m = 10
    output = "is_Grid" + str(n) + "x" + str(m) + "_colorable.cnf"
    graph = generator.create_grid(n, m)
    compute_chromatic_number(graph, filename=output)


def test_torus():
    n = 17
    m = 11
    output = "is_Torus" + str(n) + "x" + str(m) + "_colorable.cnf"
    graph = generator.create_torus(n, m)
    compute_chromatic_number(graph, filename=output)


def test_klein_bottle():
    n = 3
    m = 2
    output = "is_KB" + str(n) + "x" + str(m) + "_colorable.cnf"
    graph = generator.create_klein_bottle(n, m)
    print("graph generated")
    compute_chromatic_number(graph, filename=output)


def test_gadget_cycle():
    l = 5
    k = 7
    output = "is_GC" + str(k) + "x" + str(l) + "_colorable.cnf"
    graph = generator.create_gadget_cycle(k, l)
    print("graph generated")
    compute_chromatic_number(graph, filename=output)


def test_gadget_path():
    l = 5
    k = 7
    output = "is_GC" + str(k) + "x" + str(l) + "_colorable.cnf"
    graph = generator.create_gadget_path(k, l)
    print("graph generated")
    compute_chromatic_number(graph, filename=output)


def test_gadget_klein_bottle():
    n = 17
    m = 17
    k = 3
    output = "is_" + str(k) + "-GKB" + str(n) + "x" + str(m) + "_colorable.cnf"
    graph = generator.create_gadget_klein_bottle(n, m, k)
    print("graph generated")
    compute_chromatic_number_downward(graph, filename=output)


test_gadget_cycle()