from itertools import combinations

# Part 1: find the two entries that sum to 2020 and then multiply those two numbers together.

# Get input numbers
file = open('input', 'r')
content = file.readlines()
inputNumbers = set()
for line in content:
    inputNumbers.add(int(line))

for num in inputNumbers:
    if 2020 - num in inputNumbers:
        result = num * (2020 - num)
        print(result)
        break

# Part 2: find three numbers in your expense report that meet the same criteria

inputList = list(inputNumbers)
inputList.sort()


# test function
def test(val):
    return sum(val) == 2020


triplet = list(filter(test, list(combinations(inputList, 3))))
result = triplet[0][0] * triplet[0][1] * triplet[0][2]
print(result)
