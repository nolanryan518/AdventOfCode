import sys


def findLowestIndex(arr):
    lowestVal = sys.maxsize * 2 + 1
    lowestIdx= -1
    idx = 0
    for item in arr:
        if item < lowestVal:
            lowestVal = item
            lowestIdx = idx
        idx += 1

    return lowestIdx



def findTopElves(numElves, elfArr):
    print("Finding top {num} elves calorie total".format(num=numElves))
    topIdx = [-1 for i in range(numElves)]
    topVals = [-1 for i in range(numElves)]
    totalArr = []

    for elf in elfArr:
        elfItems = elf.split('\n')

        elfTotal = 0
        for item in elfItems:
            elfTotal += int(item)

        totalArr.append(elfTotal)

    idx = 0
    for cals in totalArr:
        topValsLowestIdx = findLowestIndex(topVals)

        if cals > topVals[topValsLowestIdx]:
            topVals[topValsLowestIdx] = cals
            topIdx[topValsLowestIdx] = idx
        idx += 1

    largestVal = 0
    for item in topVals:
        largestVal += item
    return largestVal


if __name__ == '__main__':
    # Part One
    # Read input file
    adventInput = open("input.txt", 'r')
    adventInputString = adventInput.read()

    # Split into individual elf array
    elfArr = adventInputString.split("\n\n")
    print(elfArr)

    # Part 1
    topElves = 1
    topTotal = findTopElves(topElves, elfArr)
    print(str(topTotal))


    # Part Two
    topElves = 3
    topTotal = findTopElves(topElves, elfArr)
    print(str(topTotal))