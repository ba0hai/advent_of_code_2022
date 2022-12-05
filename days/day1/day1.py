import numpy as np
import heapq

def get_input():
    with open('input') as f:
        lines = []
        line = []
        vals = f.readlines()
        for val in vals:
            if val != '\n':
                val_len = len(val)
                val = val[:val_len-1]
                line.append(int(val))
            else:
                lines.append(line)
                line = []
    return lines

def solve():
    input = get_input()
    sums = []
    for list in input:
        np_list = np.asarray(list)
        summ = np.sum(np_list)
        heapq.heappush(sums, summ)
    return sum(heapq.nlargest(3, sums))

def main():
    print("Day 1 answer here")
    ans = solve()
    print(ans)

main()