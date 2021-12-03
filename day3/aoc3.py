from collections import OrderedDict
from os import read

def main() -> None:
    with open('input_file.txt', 'r') as input_file:
        readings = [_.strip() for _ in input_file]
    ##########
    # Part 1 #
    ##########
    one_counts = {}
    for reading in readings:
        for pos, val in enumerate(list(reading)):
            if val == '1':
                one_counts[pos] = one_counts.get(pos, 0) + 1
    sorted_counts = OrderedDict(sorted(one_counts.items()))
    g_output, e_output = "", ""
    for _, v in sorted_counts.items():
        if v > len(readings)/2:
            g_output += "1"
            e_output += "0"
        else:
            g_output += "0"
            e_output += "1"
    gamma = int(g_output, 2)
    epsilon = int(e_output, 2)
    ##########
    # Part 2 #
    ##########
    # Terrible, but it works
    candidates = readings
    for i in range(0,len(readings[0])):
        one_counts = 0
        new_candidates = []
        for candidate in candidates:
            if candidate[i] == "1":
                one_counts += 1
        if one_counts >= len(candidates)/2:
            current_val = "1"
        else:
            current_val = "0"
        for candidate in candidates:
            if candidate[i] == current_val:
                new_candidates.append(candidate)
        candidates = new_candidates
        if len(candidates) == 1:
            break
    o_candidate = candidates[0]
    candidates = readings
    for i in range(0,len(readings[0])):
        one_counts = 0
        new_candidates = []
        for candidate in candidates:
            if candidate[i] == "1":
                one_counts += 1
        if one_counts >= len(candidates)/2:
            current_val = "0"
        else:
            current_val = "1"
        for candidate in candidates:
            if candidate[i] == current_val:
                new_candidates.append(candidate)
        candidates = new_candidates
        if len(candidates) == 1:
            break
    c_candidate = candidates[0]
    print(int(o_candidate,2) * int(c_candidate, 2))
        



if __name__ == '__main__':
    main()