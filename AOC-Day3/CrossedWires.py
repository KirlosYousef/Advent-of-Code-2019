#!/usr/bin/env python3


def draw_path(wire_path, step, num_of_steps, path_array):
    x = list(wire_path[-1])[0]
    y = list(wire_path[-1].values())[0]
    steps = int(step[1:]) + 1

    if step[0] == 'R':
        for i in range(1, steps):
            wire_path.append({x: y + i})
            num_of_steps += 1
            path_array.append(num_of_steps)
    if step[0] == 'U':
        for i in range(1, steps):
            wire_path.append({x + i: y})
            num_of_steps += 1
            path_array.append(num_of_steps)
    if step[0] == 'L':
        for i in range(1, steps):
            wire_path.append({x: y - i})
            num_of_steps += 1
            path_array.append(num_of_steps)
    if step[0] == 'D':
        for i in range(1, steps):
            wire_path.append({x - i: y})
            num_of_steps += 1
            path_array.append(num_of_steps)

    return wire_path, num_of_steps, path_array


def main():
    first_path = [{0: 0}]
    second_path = [{0: 0}]
    first_path_counter = 0
    second_path_counter = 0
    first_path_array = []
    second_path_array = []

    with open('input.txt') as r:
        wires = r.readlines()
        i = 0
        for wire in wires:
            for step in wire.split(','):
                if i == 0:
                    first_path, first_path_counter, first_path_array = draw_path(first_path, step,
                                                                                 first_path_counter,
                                                                                 first_path_array)
                elif i == 1:
                    second_path, second_path_counter, second_path_array = draw_path(second_path, step,
                                                                                    second_path_counter,
                                                                                    second_path_array)
            i += 1

    intersection_points = []

    print('Loading...')

    first_counter = -1
    for p in first_path:
        second_counter = -1
        for s in second_path:
            if p == s and p != {0: 0}:
                intersection_points.append(first_path_array[first_counter] + second_path_array[second_counter])
            second_counter += 1
        first_counter += 1

    print(min(intersection_points))


if __name__ == "__main__":
    main()
