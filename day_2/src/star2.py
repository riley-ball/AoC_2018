def main():

    # LUL get fucking hacked, iterating through a file with a nested for loop doesn't work????

    big_list = []
    with open("day_2/input1.txt", "r") as input1:
        for line in input1:
            big_list.append(line)



    # intial line
    for line in big_list:
        # line to be checked
        for check in big_list:
            wrong_letter = []
            # count must == 1
            count = 0
            for i in range(len(line)):
                if len(line) != len(check):
                    break
                if line[i] != check[i]:
                    count += 1
                    wrong_letter.append(line[i])
            if count == 1:
                print(line, check, wrong_letter[0])



if __name__ == "__main__":
    main()