
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
