#!/usr/bin/env python3

INPUT_RANGE = range(387638, 919124)


def main():

    passwords = []

    for i in INPUT_RANGE:
        pass_array = [int(x) for x in str(i)]

        flag = True

        for j in range(0, 6):
            for r in pass_array[j:]:
                if pass_array[j] > r:
                    flag = False

        if flag:
            flag2 = 10
            for j in range(0, 5):
                if j < 4 and pass_array[j] == pass_array[j+1] == pass_array[j+2]:
                    flag2 = pass_array[j]
                    pass
                elif pass_array[j] == pass_array[j+1] and pass_array[j] != flag2:
                    passwords.append(pass_array)
                    break

    # print(passwords)

    print('The number of different passwords within the range given:', len(passwords))


if __name__ == "__main__":
    main()
