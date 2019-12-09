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
                        if int(opcode[-2:]) > 8:
                            opcode = opcode[:-1] + '0' + opcode[-1]
                        else:
                            opcode = '0' + opcode

                mode1 = int(opcode[1])
                mode2 = int(opcode[0])
                opcode = round(int(opcode[-2:]))

            first_ind = numbers_array[i + 1]
            if mode1 == 1:
                first_ind = i + 1

            if opcode in [1, 2, 5, 6, 7, 8]:
                second_ind = numbers_array[i + 2]
                if mode2 == 1:
                    second_ind = i + 2

                third_ind = numbers_array[i + 3]

                if opcode == 1:
                    out_put = numbers_array[first_ind] + numbers_array[second_ind]
                    numbers_array[third_ind] = out_put
                    i += 4

                elif opcode == 2:
                    out_put = numbers_array[first_ind] * numbers_array[second_ind]
                    numbers_array[third_ind] = out_put
                    i += 4

                elif opcode == 5:     # jump-if-true
                    if numbers_array[first_ind] != 0:
                        i = numbers_array[second_ind]
                    else:
                        i += 3

                elif opcode == 6:     # jump-if-false
                    if numbers_array[first_ind] == 0:
                        i = numbers_array[second_ind]
                    else:
                        i += 3

                elif opcode == 7:     # less than
                    if numbers_array[first_ind] < numbers_array[second_ind]:
                        numbers_array[third_ind] = 1
                    else:
                        numbers_array[third_ind] = 0
                    i += 4

                elif opcode == 8:     # equals
                    if numbers_array[first_ind] == numbers_array[second_ind]:
                        numbers_array[third_ind] = 1
                    else:
                        numbers_array[third_ind] = 0
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
