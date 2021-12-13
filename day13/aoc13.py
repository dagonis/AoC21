from dataclasses import dataclass
from typing import List

@dataclass
class Paper:
    raw_points: List
    max_x: int = 0
    max_y: int = 0

    def __post_init__(self):
        self.points = []
        for point in self.raw_points:
            x, y = [int(_) for _ in point.split(',')]
            self.points.append((int(x), int(y)))
            self.max_x = x if x > self.max_x else self.max_x
            self.max_y = y if y > self.max_y else self.max_y
        self.grid = [['.' for _ in range(self.max_x+1)] for _ in range(self.max_y+1)]
        for position in self.points:
            self.grid[position[1]][position[0]] = "#"

    def fold(self, axis, index):
        top_half = self.grid[:index] if axis == 'y' else [_[:index] for _ in self.grid]
        bottom_half = self.grid[index+1:][::-1] if axis == 'y' else [_[index+1:][::-1] for _ in self.grid]
        for x in range(len(top_half)):
            for y in range(len(top_half[x])):
                top_half[x][y] = "." if top_half[x][y] == "." and bottom_half[x][y] == "." else "#"
        self.grid = top_half
            
    def __str__(self):
        return "\n".join(["".join([_.replace('.', ' ') for _ in _]) for _ in self.grid])        


def main() -> None:
    with open('input.txt', 'r') as input_file:
        lines = [_.strip() for _ in input_file if not _.strip() == '']
    points = [_ for _ in lines if not _.startswith('f')]
    instructions = [_.lstrip('fold along ').split('=') for _ in lines if _.startswith('f')]
    p = Paper(points)
    point_counts = []
    for instruction in instructions:
        p.fold(instruction[0], int(instruction[1]))
        point_counts.append(str(p).count("#"))
    print(point_counts[0])
    print(p)


if __name__ == '__main__':
    main()