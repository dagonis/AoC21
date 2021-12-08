from dataclasses import dataclass
from os import read


@dataclass
class Reading:
    raw_input: str

    def __post_init__(self):
        self.input, self.output = self.raw_input.split(' | ')
        known_map = set()
        known_ones = set()
        for digit in self.input.split():
            if len(digit) == 2:
                known_map.update(digit)
                known_ones.update(digit)
            elif len(digit) == 4:
                known_map.update(digit)
            elif len(digit) == 3:
                known_map.update(digit)
        self.input_digits, self.output_digits = [], []
        for digit in self.input.split():
            self.input_digits.append(Digit(digit, known_map, known_ones))
        for digit in self.output.split():
            self.output_digits.append(Digit(digit, known_map, known_ones))
    
    @property
    def full_output(self):
        return "".join(str(_.output) for _ in self.output_digits)

        

@dataclass
class Digit:
    input_str: str
    digit_map: set
    ones: set

    @property
    def output(self):
        if len(self.input_str) == 2:
            return 1
        elif len(self.input_str) == 3:
            return 7
        elif len(self.input_str) == 4:
            return 4
        elif len(self.input_str) == 7:
            return 8
        elif len(self.input_str) == 5:
            if len(self.digit_map.difference(self.input_str)) == 2:
                return 2
            elif len(self.digit_map.difference(self.input_str)) == 1:
                if len(self.ones.difference(self.input_str)) == 0:
                    return 3
                else: 
                    return 5
        elif len(self.input_str) == 6:
            if len(self.digit_map.difference(self.input_str)) == 0:
                return 9
            elif len(self.digit_map.difference(self.input_str)) == 1:
                if len(self.ones.difference(self.input_str)) == 0:
                    return 0
                else: 
                    return 6
        else:
            return "Unknown"


def main() -> None:
    with open('input.txt', 'r') as input_file:
        raw_readings = [_.strip() for _ in input_file]
    readings = [Reading(_) for _ in raw_readings]
    known_outs = 0
    for reading in readings:
        print(reading.full_output)
        known_outs += int(reading.full_output)
    print(known_outs)
            
    

if __name__ == '__main__':
    main()