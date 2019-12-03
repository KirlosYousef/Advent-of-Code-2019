#!/usr/bin/env python3


def calc(mass):
    return int((mass/3)) - 2


def main():
    total = 0

    with open('input.txt', 'r') as f:
        for line in f:
            mass = calc(int(line))
            while mass > 0:
                # print(mass)
                total += mass
                mass = calc(mass)

    print(total)


if __name__ == "__main__":
    main()
