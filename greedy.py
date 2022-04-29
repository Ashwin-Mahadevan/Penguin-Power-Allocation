
def create_covermap(D, Rs, cities):
    """ Precomputes the set of cities that would be covered by placing a tower at (x, y). Specifically, returns a dictionary mapping each potential tower location (x, y) to a set containing the coordinates of the cities that such a tower would cover. """

    covered_by = dict()

    for x in range(D):
        for y in range(D):

            covered = set()

            for city in cities:

                X, Y = city
                if (x - X)**2 + (y - Y)**2 <= Rs**2:
                    covered.add(city)

            covered_by[(x, y)] = covered
    
    return covered_by
