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
    time = defaultdict(int)
    guard = ""
    sleep = ""
    for k in sort:
        v = storage[k]
        if len(v.split(" ")) == 4:
            guard = v.split(" ")[1]
            sleep = ""
        elif v.split(" ")[0] == "falls":
            sleep = k
        else:
            if int(sleep.split("-")[3]) == 23:
                if int(k.split("-")[3]) == 23:
                    time[guard] += int(k.split("-")[4]) - int(sleep.split("-")[4])
                else:
                    time[guard] += (60 - int(k.split("-")[4])) + int(sleep.split("-")[4])
            else:
                time[guard] += int(k.split("-")[4]) - int(sleep.split("-")[4])

    guardid = sorted(time.items(), key = lambda kv: kv[1], reverse = True)[0][0]
    commontime = defaultdict(int)

    for k in sort:
        v = storage[k]
        if len(v.split(" ")) == 4:
            guard = v.split(" ")[1]
            if guard == guardid:
                pass
            else:
                guard = ""
                sleep = ""
        elif guard == guardid and v.split(" ")[0] == "falls":
            sleep = k
        elif guard == guardid:
            if int(sleep.split("-")[3]) == 23:
                if int(k.split("-")[3]) == 23:
                    for i in range(int(sleep.split("-")[4]), int(k.split("-")[4]) + 1):
                     commontime[i] += 1
                else:
                    for i in range(int(sleep.split("-")[4]), 60):
                        commontime[i] += 1
                    for i in range(0, int(k.split("-")[4]) + 1):
                        commontime[i] += 1
            else:
                for i in range(int(sleep.split("-")[4]), int(k.split("-")[4]) + 1):
                    commontime[i] += 1
    print(int(guardid[1:]) * sorted(commontime.items(), key = lambda kv: kv[1], reverse = True)[1][0])



if __name__ == "__main__":
    main()