from random import randrange

def generate(path, N, D, Rs, Rp):

    with open(path, 'w') as file:

        file.write(f'{N}\n')
        file.write(f'{D}\n')
        file.write(f'{Rs}\n')
        file.write(f'{Rp}\n')

        cities = set()
        while len(cities) < N:
            
            city = (randrange(0, D), randrange(0, D))

            if city not in cities:
                cities.add(city)
                file.write(f'{city[0]} {city[1]}\n')

if __name__ == '__main__':
    generate('inputs/small.in', 22, 30, 3, 8)
    generate('inputs/medium.in', 53, 50, 3, 10)
    generate('inputs/large.in', 198, 100, 3, 14)
