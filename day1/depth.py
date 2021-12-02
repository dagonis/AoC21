def main():
    depths = []
    with open('input', 'r') as input_file:
        for line in input_file:
            depths.append(int(line.strip()))
    depths = [_ for _ in enumerate(depths)]
    inc, dec, same = 0, 0, 0
    ##########
    # Part 1 #
    ##########
    for i, v in depths:
        current, previous = v, depths[i-1][1]
        if current > previous:
            inc += 1
        else:
            dec += 1
    print(inc, dec)
    ##########
    # Part 2 #
    ##########
    inc, dec, same = 0, 0, 0
    for i, v in depths:
        if i < len(depths) - 2:
            current_window = sum([v, depths[i+1][1], depths[i+2][1]])
            previous_windows = current_window
            if not i == 0 and not i == 1:
                previous_windows = sum([v, depths[i-1][1], depths[i+1][1]])
            else:
                pass
            if current_window > previous_windows:
                inc += 1
            elif current_window < previous_windows:
                dec += 1
            else:
                same += 1
    print(inc, dec, same)

if __name__ == '__main__':
    main()