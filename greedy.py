from itertools import product
from utils import additional_penalty, dist_sq, penalty


def create_covermap(D, Rs, cities):
    """ Precomputes the set of cities that would be covered by placing a tower at (x, y). Specifically, returns a dictionary mapping each potential tower location (x, y) to a set containing the coordinates of the cities that such a tower would cover. """

    covered_by = dict()

    for point in product(range(D), range(D)):

        covered = set()

        for city in cities:

            if dist_sq(point, city) < Rs**2:
                covered.add(city)

        if len(covered) > 0:
            covered_by[point] = covered

    return covered_by


def solve_greedy(D, Rs, Rp, cities):

    covered_by = create_covermap(D, Rs, cities)

    uncovered_cities = set(cities)

    towers = list()
    nearby_counts = list()

    def uncovered_count(tower):
        covered_by[tower].intersection_update(uncovered_cities)
        return len(covered_by[tower])

    while uncovered_cities:

        best_tower = max(
            covered_by,
            key=lambda new_tower: (uncovered_count(new_tower), -additional_penalty(
                towers, nearby_counts, new_tower, Rp)),
        )

        nearby_best = 0

        for i in range(len(towers)):
            if dist_sq(towers[i], best_tower) <= Rp**2:
                nearby_counts[i] += 1
                nearby_best += 1

        towers.append(best_tower)
        nearby_counts.append(nearby_best)
        uncovered_cities.difference_update(covered_by[best_tower])

    return towers
