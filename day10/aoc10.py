from collections import deque
from dataclasses import dataclass

start_delims = ["(", "[", "{", "<"] 
end_delims = [")", "]", "}", ">"]
corrupt_values = {")": 3, "]": 57, "}": 1197, ">": 25137}
completion_values = {")": 1, "]": 2, "}": 3, ">": 4}

@dataclass
class CodeLine:
    raw_input: str
    corrupt_character: str = None
    completion_delims: str = None

    @property
    def corrupt(self):
        delim_stack = deque()
        for delim in self.raw_input:
            if delim in start_delims:
                delim_stack.append(delim)
            if delim in end_delims:
                _d = delim_stack.pop()
                if not start_delims.index(_d) == end_delims.index(delim):
                    self.corrupt_character = delim
                    return True
        return False

    @property
    def complete(self):
        balance = 0
        s, e = [], []
        for delim in self.raw_input:
            if delim in start_delims:
                s.append(delim)
                balance += 1
            elif delim in end_delims:
                e.append(delim)
                balance -= 1
        print(balance, s, e)
        if balance == 0:
            return True
        return False

    def complete_line(self):
        delim_stack = deque()
        self.completion_delims = ""
        for delim in self.raw_input:
            if delim in start_delims:
                delim_stack.append(delim)
            elif delim in end_delims:
                _d = delim_stack.pop()
        while len(delim_stack) > 0:
            _d = delim_stack.pop()
            self.completion_delims += end_delims[start_delims.index(_d)]
        return self.completion_delims



def main() -> None:
    with open("input.txt", 'r') as input_file:
        raw_code_lines = [_.strip() for _ in input_file]
    code_lines = [CodeLine(_) for _ in raw_code_lines]
    corrupt_characters = []
    incomplete_lines = []
    for code_line in code_lines:
        if code_line.corrupt:
            corrupt_characters.append(code_line.corrupt_character)
        else:
            incomplete_lines.append(code_line)
    corrupt_sum = 0
    for c in corrupt_characters:
        corrupt_sum += corrupt_values[c]
    print(corrupt_sum)
    completions = []
    for line in incomplete_lines:
        completions.append(line.complete_line())
    completion_scores = []
    for completion in completions:
        score = 0
        for c in completion:
            score *= 5
            score += completion_values[c]
        completion_scores.append(score)
    completion_scores.sort()
    print(completion_scores[len(completion_scores)//2])


if __name__ == '__main__':
    main()