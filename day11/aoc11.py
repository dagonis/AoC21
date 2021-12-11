from dataclasses import dataclass
from typing import List

@dataclass
class OctoField:
    Octos: List

    def step(self):
        more_flashes = False
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for r in self.Octos:
            for o in r:
                o.value += 1
                if o.value > 9:
                    more_flashes = True
        while more_flashes:
            more_flashes = False
            for r in self.Octos:
                for o in r:
                    if o.value > 9 and not o.flashed:
                        o.flashed = True
                        for x, y in neighbors:
                            if sum([o.x, x]) > -1 and sum([o.y, y]) > -1:
                                try:
                                    self.Octos[sum([o.x, x])][sum([o.y, y])].value += 1
                                except Exception as e:
                                    pass
            for r in self.Octos:
                for o in r:
                    if o.value > 9 and not o.flashed:
                        more_flashes = True
        flashes = 0
        for r in self.Octos:
            for o in r:
                if o.value > 9:
                    flashes += 1
                    o.value = 0
                    o.flashed = False
        return flashes

    def all_flashed(self):
        all_flashed = True
        for r in self.Octos:
            for o in r:
                if not o.value == 0:
                    all_flashed = False
        return all_flashed

    def print_field(self):
        for r in self.Octos:
            print("".join([str(_.value) for _ in r]))
                    

@dataclass
class DumboOcto:
    value: int
    x: int
    y: int
    flashed: bool = False


def main() -> None:
    with open("input.txt", "r") as input_file:
        raw_values = [_ for _ in [_.strip() for _ in input_file]]
    field = OctoField([])
    for ri, row in enumerate(raw_values):
        _row = []
        for ci, n in enumerate(list(row)):
            _row.append(DumboOcto(int(n), ri, ci))
        field.Octos.append(_row)
    field.print_field()
    print("\n")
    flashes = 0
    for n in range(1000):
        flashes += field.step()
        if field.all_flashed():
            print(n+1)
    print(flashes)
    


if __name__ == '__main__':
    main()