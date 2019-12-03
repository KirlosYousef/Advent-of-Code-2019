#!/usr/bin/env python3


def int_code(numbers_array):
    for i in range(0, len(numbers_array) - 1, 4):
        opcode = numbers_array[i]
        first_ind = numbers_array[i + 1]
        second_ind = numbers_array[i + 2]
        third_ind = numbers_array[i + 3]

        if opcode == 1:
            out_put = numbers_array[first_ind] + numbers_array[second_ind]
            numbers_array[third_ind] = out_put

        elif opcode == 2:
            out_put = numbers_array[first_ind] * numbers_array[second_ind]
            numbers_array[third_ind] = out_put

        elif opcode == 99:
            break

        else:
            print('Something wrong!')
    return numbers_array


def main():
    with open('input.txt') as r:
        numbers = r.readlines()[0]
        for noun in range(100):
            for verb in range(100):
                numbers_array = [int(num) for num in str(numbers).split(',')]
                numbers_array[1] = noun
                numbers_array[2] = verb
                numbers_array = int_code(numbers_array)

                if numbers_array[0] == 19690720:
                    print('The Noun and the Verb needed to obtain 19690720 are:', noun, verb)
                    break


if __name__ == "__main__":
    main()
