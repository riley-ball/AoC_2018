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
    guards = defaultdict(int)
    guard = ""
    sleep = ""

    # iterate through all guards and record the nights they fall asleep - 
    # looking for guard with most nights slept on a specific date
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
                    for i in range(int(sleep.split("-")[4]), int(k.split("-")[4]) + 1):
                        time[i+2300] += 1
                else:
                    for i in range(int(sleep.split("-")[4]), 60):
                        time[i+2300] += 1
                    for i in range(0, int(k.split("-")[4]) + 1):
                        time[i] += 1
            else:
                for i in range(int(sleep.split("-")[4]), int(k.split("-")[4]) + 1):
                    time[i] += 1
    commontime = sorted(time.items(), key = lambda kv: kv[1], reverse = True)[0][0]
    print(sorted(time.items(), key = lambda kv: kv[1], reverse = True))
    
    # # find most common guard for the time

    # commonguard = defaultdict(int)

    # for k in sort:
    #     v = storage[k]
    #     if len(v.split(" ")) == 4:
    #         guard = v.split(" ")[1]
    #         sleep = ""
    #     elif v.split(" ")[0] == "falls":
    #         sleep = k
    #     else:
    #         if int(sleep.split("-")[3]) == 23:
    #             if int(k.split("-")[3]) == 23:
    #                 for i in range(int(sleep.split("-")[4]), int(k.split("-")[4]) + 1):
    #                     if i == commontime:
    #                         commonguard[guard] += 1
    #             else:
    #                 for i in range(int(sleep.split("-")[4]), 60):
    #                     if i == commontime:
    #                         commonguard[guard] += 1
    #                 for i in range(0, int(k.split("-")[4]) + 1):
    #                     if i == commontime:
    #                         commonguard[guard] += 1
    #         else:
    #             for i in range(int(sleep.split("-")[4]), int(k.split("-")[4]) + 1):
    #                 if i == commontime:
    #                         commonguard[guard] += 1
    # print(sorted(commonguard.items(), key = lambda kv: kv[1], reverse = True))
    # # print(commontime, theguard)
    # # print(commontime * int(theguard[1:]))

if __name__ == "__main__":
    main()