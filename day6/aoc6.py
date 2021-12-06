from collections import OrderedDict
from dataclasses import dataclass

@dataclass
class LanternFish:
    timer: int

    def inc_day(self):
        self.timer = self.timer - 1 if self.timer > 0 else 6

    def __repr__(self):
        return str(self.timer)

def main() -> None:
    with open('input.txt', 'r') as input_file:
        timers = [int(_) for _ in [_.strip() for _ in input_file][0].split(',')]
    ##########
    # Part 1 #
    ##########
    lantern_fishes = []
    for timer in timers:
        lantern_fishes.append(LanternFish(timer))
    new_fishes = 0
    for n in range(80):
        for _ in range(new_fishes):
            lantern_fishes.append(LanternFish(9))
        new_fishes = 0
        for lantern_fish in lantern_fishes:
            lantern_fish.inc_day()
            if lantern_fish.timer == 0:
                new_fishes += 1
    print(len(lantern_fishes))
    ##########
    # Part 2 #
    ##########
    lantern_fishes = {}
    for timer in timers:
        lantern_fishes[timer] = lantern_fishes.get(timer, 0) + 1
    for _ in range(256):
        new_fish_state = {}
        for k in sorted(lantern_fishes.keys(), reverse=True):
            if k >= 1:
                new_fish_state[k-1] = lantern_fishes.get(k)
            elif k == 0:
                new_fish_state[6] = new_fish_state.get(6, 0) + lantern_fishes[k]
                new_fish_state[8] = lantern_fishes.get(0, 1)
        lantern_fishes = new_fish_state
    print(sum(lantern_fishes.values()))



if __name__ == '__main__':
    main()