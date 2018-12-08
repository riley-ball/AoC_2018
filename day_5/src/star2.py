from collections import defaultdict
import string

# answer: 10774, why am I 1 off??

def main():
    inputfile = ""
    letters = string.ascii_lowercase
    for i in open('day_5/input.txt', 'r'):
        inputfile += i
    prevlower = ""
    prevupper = ""
    hasChanged = True
    storagedic = defaultdict(int)
    for ascletter in letters:
        newinput = inputfile.replace(ascletter, '')
        newinput = newinput.replace(ascletter.upper(), '')
        hasChanged = True
        while hasChanged:
            storage = ""
            changes = 0
            for letter in newinput:
                if letter.islower():
                    if prevupper.lower() == letter:
                        storage = storage[0:-1]
                        prevlower = ""
                        prevupper = ""
                        changes += 1
                    else:
                        storage += letter
                        prevlower = letter
                        prevupper = ""
                if letter.isupper():
                    if prevlower.upper() == letter:
                        storage = storage[0:-1]
                        prevlower = ""
                        prevupper = ""
                        changes += 1
                    else:
                        storage += letter
                        prevupper = letter
                        prevlower = ""
            newinput = storage
            if changes == 0:
                print(ascletter, len(storage))
                storagedic[ascletter] = len(storage)
                hasChanged = False
    print(sorted(storagedic.items(), key = lambda kv: kv[1], reverse = False))


if __name__ == "__main__":
    main()