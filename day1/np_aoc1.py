import numpy as np

def main() -> None:
    with open('input', 'r') as input_file:
        depths = np.array([_.rstrip() for _ in input_file])
    # print([("inc", v, i) for i, v in enumerate(depths) if depths[i-1] < depths[i]])
    print(sum([i2 > i1 for i1, i2 in zip(depths, depths[1:])]))

if __name__ == '__main__':
    main()