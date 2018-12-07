from collections import defaultdict
def main():
    storage = {}
    for line in open('day_4/input.txt', 'r'):
        timestamp = line[1:17]
        timestamp = timestamp.split(" ")
        timestamp = "-".join(timestamp)
        timestamp = timestamp.split(":")
        timestamp = "-".join(timestamp)
        storage[timestamp] = line[19:]

    sort = sorted(storage, key=lambda d: tuple(map(int, d.split('-'))))
        
if __name__ == "__main__":
    main()