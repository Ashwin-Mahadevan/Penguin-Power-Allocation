from math import exp
from os import listdir
from itertools import product


def dist_sq(A, B):
    x0, y0 = A
    x1, y1 = B
    return (x1 - x0)**2 + (y1 - y0)**2


def additional_penalty(towers, counts, new_tower, Rp):

    nearby_new = 0
    penalty = 0

    for i in range(len(towers)):
        if dist_sq(towers[i], new_tower) <= Rp**2:
            penalty += exp(0.17 * (counts[i] + 1))
            nearby_new += 1
        else:
            penalty += exp(0.17 * counts[i])

    return penalty + exp(0.17 * nearby_new)


def penalty(towers, Rp):

    counts = [0 for _ in towers]

    for i, j in product(range(len(towers)), range(len(towers))):

        if i != j and dist_sq(towers[i], towers[j]) <= Rp**2:
            counts[i] += 1
            counts[j] += 1

    return sum(exp(0.17 * count) for count in counts)


def read_board(path):

    with open(path, 'r') as file:

        skip_comments = lambda line: line[0] != '#'
        lines = filter(skip_comments, file)

        N = int(next(lines))
        D = int(next(lines))
        Rs = int(next(lines))
        Rp = int(next(lines))

        cities = list()

        for line in lines:
            x, y = line.split()
            cities.append((int(x), int(y)))

    assert len(cities) == N

    return N, D, Rs, Rp, cities


def write_solution(path, towers):
    """ Takes a single solution, given as a list of towers to place, and writes it out to a given file path. """

    with open(path, 'w') as file:

        file.write(f'{len(towers)}\n')

        for tower in towers:
            file.write(f'{tower[0]} {tower[1]}\n')


def get_solutions(solver):
    """ Runs a given algorithm on the class inputs, and writes using the correct output format. """

    problem_paths = list()

    for filename in listdir('inputs/small'):
        problem_paths.append(f'small/{filename[:-3]}')

    for filename in listdir('inputs/medium'):
        problem_paths.append(f'medium/{filename[:-3]}')

    for filename in listdir('inputs/large'):
        problem_paths.append(f'large/{filename[:-3]}')

    for problem_path in problem_paths:

        N, D, Rs, Rp, cities = read_board('inputs/' + problem_path + '.in')
        towers = solver(D, Rs, Rp, cities)

        write_solution('outputs/' + problem_path + '.out', towers)
