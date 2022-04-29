def create_covermap(D, Rs, cities):
    """ Precomputes the set of cities that would be covered by placing a tower at (x, y). Specifically, returns a dictionary mapping each potential tower location (x, y) to a set containing the coordinates of the cities that such a tower would cover. """

    covers = dict()

    for x in range(D):
        for y in range(D):

            covered = set()

            for city in cities:

                X, Y = city
                if (x - X)**2 + (y - Y)**2 <= Rs**2:
                    covered.add(city)

            covers[(x, y)] = covered

    return covers


def solve_greedy(D, Rs, Rp, cities):

    covers = create_covermap(D, Rs, cities)

    uncovered = set(cities)

    towers = list()

    def uncovered_size(c):
        covers[c].intersection_update(uncovered)
        return len(covers[c])

    while uncovered:

        best_tower = max(covers, key=uncovered_size)
        towers.append(best_tower)
        uncovered.difference_update(covers[best_tower])

    return towers
