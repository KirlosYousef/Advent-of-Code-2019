#!/usr/bin/env python3


def int_code(numbers_array, input_val):

    i = 0

    while i in range(len(numbers_array)):

        opcode = numbers_array[i]
        if opcode == 99:
            return

        else:
            mode1 = 0
            mode2 = 0
            if len(str(opcode)) > 1:
                opcode = str(opcode)
                if len(opcode) < 4:
                    for _ in range(4 - len(opcode)):
                        opcode = '0' + opcode

                mode1 = int(opcode[1])
                mode2 = int(opcode[0])
                opcode = round(int(opcode[-2:]))

            first_ind = numbers_array[i + 1]
            if mode1 == 1:
                first_ind = i + 1

            if opcode == 1 or opcode == 2:
                second_ind = numbers_array[i + 2]
                if mode2 == 1:
                    second_ind = i + 2

                third_ind = numbers_array[i + 3]
                if opcode == 1:
                    out_put = numbers_array[first_ind] + numbers_array[second_ind]
                    numbers_array[third_ind] = out_put

                elif opcode == 2:
                    out_put = numbers_array[first_ind] * numbers_array[second_ind]
                    numbers_array[third_ind] = out_put

                i += 4

            elif opcode == 3:
                out_put = input_val
                numbers_array[first_ind] = out_put
                i += 2

            elif opcode == 4:
                out_put = numbers_array[first_ind]
                print(out_put)
                i += 2

            else:
                print('Something wrong! at', opcode)
                return


def main():
    with open('input.txt') as r:
        numbers = r.readlines()[0]
        numbers_array = [int(num) for num in str(numbers).split(',')]
        inp = input('Enter the input value: ')
        int_code(numbers_array, int(inp))


if __name__ == "__main__":
    main()
