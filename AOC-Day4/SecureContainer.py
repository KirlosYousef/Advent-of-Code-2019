#!/usr/bin/env python3

INPUT_RANGE = range(387638, 919124)


def main():

    passwords = []

    for i in INPUT_RANGE:
        pass_array = [int(x) for x in str(i)]

        flag = True

        for j in range(0, 6):  # 387638
            for r in pass_array[j:]:
                if pass_array[j] > r:
                    flag = False

        if flag:

            # If this number is prohibited because it has been repeated more than twice!
            prohibited_num = 10     # 10 is the default value cause it's out of the range 0 to 9.

            for j in range(0, 5):
                if j < 4 and pass_array[j] == pass_array[j+1] == pass_array[j+2]:
                    prohibited_num = pass_array[j]

                elif pass_array[j] == pass_array[j+1] and pass_array[j] != prohibited_num:
                    passwords.append(pass_array)
                    break

    print('The number of different passwords within the range given:', len(passwords))


if __name__ == "__main__":
    main()
