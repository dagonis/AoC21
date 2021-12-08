def main() -> None:
    with open("input.txt", "r") as input_file:
        crabs = [int(_) for _ in [_.strip() for _ in input_file][0].split(",")]
    all_movements = []
    for n in range(max(crabs)+1):
        movements = []
        for crab in crabs:
            fuel_units = abs(crab - n)
            cost = sum([_ for _ in range(fuel_units + 1)]) # Part 2
            movements.append(cost)
        all_movements.append(movements)
    print(min([sum(movement) for movement in all_movements]))


if __name__ == '__main__':
    main()