from itertools import product
from utils import dist_sq, penalty


def create_covermap(D, Rs, cities):
    """ Precomputes the set of cities that would be covered by placing a tower at (x, y). Specifically, returns a dictionary mapping each potential tower location (x, y) to a set containing the coordinates of the cities that such a tower would cover. """

    covered_by = dict()

    for point in product(range(D), range(D)):

        covered = set()

        for city in cities:

            if dist_sq(point, city) < Rs**2:
                covered.add(city)

        covered_by[point] = covered

    return covered_by


def solve_greedy(D, Rs, Rp, cities):

    covered_by = create_covermap(D, Rs, cities)

    uncovered_cities = set(cities)

    towers = list()

    def uncovered_count(tower):
        covered_by[tower].intersection_update(uncovered_cities)
        return len(covered_by[tower])

    while uncovered_cities:

        best_tower = max(
            covered_by, key=lambda tower:
            (uncovered_count(tower), penalty(towers + [tower], Rp)))
        towers.append(best_tower)
        uncovered_cities.difference_update(covered_by[best_tower])

    return towers
