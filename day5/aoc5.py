import itertools
from collections import Counter
from dataclasses import dataclass

@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def __post_init__(self):
        if self.x1 == self.x2:
            self.all_points = [(self.x1, y) for y in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1)]
        elif self.y1 == self.y2:
            self.all_points = [(x, self.y1) for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1)]
        else:
            self.all_points = [(self.x1, self.y1)]
            while not self.all_points[-1] == (self.x2, self.y2):
                self.all_points.append(
                    (self.all_points[-1][0] + 1 if self.x2 > self.x1 else self.all_points[-1][0] - 1, 
                     self.all_points[-1][1] + 1 if self.y2 > self.y1 else self.all_points[-1][1] - 1)
                                       )

def main() -> None:
    with open('input.txt', 'r') as input_file:
        raw_points = [_.strip().replace(" -> ", ",") for _ in input_file]
    lines = [Line(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in [_.split(",") for _ in raw_points]]
    vent_points = list(itertools.chain.from_iterable([_.all_points for _ in lines]))
    print(len([_ for _ in Counter(vent_points).values() if _ >1]))

if __name__ == '__main__':
    main()