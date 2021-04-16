import sys
import math

def getInput(n_lines):
    print("Input lines: ", file=sys.stderr)
    input_lines = []
    for _ in range(n_lines):
        new_line = int(input())
        input_lines.append(new_line)
        print(new_line, file=sys.stderr)

    return input_lines

def getMinimumDifference(array):
    array.sort()
    
    min_item_diff = None
    prev_item = array[0]
    for item in array[1 : len(array)]:
        item_diff = abs(prev_item - item)
        prev_item = item
        if min_item_diff is None or min_item_diff > item_diff:
            min_item_diff = item_diff
            if min_item_diff == 0:
                break
       
    return min_item_diff


n_lines = int(input())
print("Number of items: ", n_lines, file=sys.stderr)

print(
    getMinimumDifference(
        getInput(n_lines)
    )
)