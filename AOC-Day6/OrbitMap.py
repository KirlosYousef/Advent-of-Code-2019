#!/usr/bin/env python3


def search(orbits, planet, w_count):
    return_val = 0

    for prev in orbits:

        current_count = w_count
        prev_first = prev[0]
        prev_second = prev[1]

        if planet == prev_second:
            if prev_first != 'COM':
                current_count += 1
                return_val = search(orbits, prev_first, current_count)
            else:
                current_count += 1
                return_val = current_count
                
    return return_val


def main():
    with open('input.txt', 'r') as r:

        lines = [line.rstrip() for line in r.readlines()]
        orbits = [line.split(')') for line in lines]

        planets = []
        for i in range(len(orbits)):
            for j in range(len(orbits[i])):
                if orbits[i][j] != 'COM':
                    planets.append(orbits[i][j])
        planets = list(set(planets))

        total_number = 0
        for planet in planets:
            number = search(orbits, planet, 0)
            total_number += number

    print("the total number of direct and indirect orbits: s" + str(total_number))


if __name__ == "__main__":
    main()
