def main():
    count = 0
    number_list = [0]
    flag = 0
    list_count = 0
    while flag == 0:
        with open ("./input.txt", "r") as input:
            list_count += 1
            print(list_count)
            for line in input:
                count += int(line)
                if count in number_list:
                    print(count)
                    flag = 1
                    break
                number_list.append(count)

if __name__ == "__main__":
    main()