from collections import defaultdict

# answer: 10774, why am I 1 off??

def main():
    inputfile = ""
    for i in open('day_5/input.txt', 'r'):
        inputfile += i
    prevlower = ""
    prevupper = ""
    hasChanged = True
    while hasChanged:
        storage = ""
        changes = 0
        for letter in inputfile:
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
        inputfile = storage
        print(len(storage), changes)
        if changes == 0:
            hasChanged = False



if __name__ == "__main__":
    main()