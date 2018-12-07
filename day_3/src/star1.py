from collections import defaultdict
def main():
    C = defaultdict(int)
    for line in open('day_3/input.txt', 'r'):
        words = line.split()
        x,y = words[2].split(',')
        x,y = int(x), int(y[:-1])
        w,h = words[3].split('x')
        w,h = int(w), int(h)
        for dx in range(w):
            for dy in range(h):
                C[(x+dx, y+dy)] += 1
                
    ans = 0
    for (r,c),v in C.items():
        if v >= 2:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()