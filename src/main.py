def main():
    count = 0
    with open ("./input.txt", "r") as input:
        for line in input:
                count += int(line)
    print(count)

if __name__ == "__main__":
    main()