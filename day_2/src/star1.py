def main():
    two_letters = 0
    three_letters = 0
    with open ("day_2/input.txt", "r") as input:
        for line in input:
            list_letters = []
            num_two = 0
            num_three = 0
            for index in line:
                if index not in list_letters:
                    list_letters.append(index)
                    count = 0
                    for letter in line:
                        if letter == index:
                            count += 1
                    if count == 2 and num_two == 0:
                        two_letters += 1
                        num_two += 1
                    elif count == 3 and num_three == 0:
                        three_letters += 1
                        num_three += 1
    print(two_letters, "*", three_letters, "=", two_letters * three_letters)

if __name__ == "__main__":
    main()