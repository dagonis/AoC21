from dataclasses import dataclass

@dataclass
class Submarine:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0

def main() -> None:
    with open('input', 'r') as instruction_file:
        instructions = [_.strip() for _ in instruction_file]
    ##########
    # Part 1 #
    ##########
    sub = Submarine()
    for instruction in instructions:
        match instruction.split():
            case ['down', number]:
                sub.depth += int(number)
            case ['up', number]:
                sub.depth -= int(number)
            case ['forward', number]:
                sub.horizontal += int(number)
            case other:
                print("Unknown Instruction")
    print(sub)
    print(sub.depth * sub.horizontal)
    ##########
    # Part 2 #
    ##########
    sub = Submarine()
    for instruction in instructions:
        match instruction.split():
            case ['down', number]:
                sub.aim += int(number)
            case ['up', number]:
                sub.aim -= int(number)
            case ['forward', number]:
                sub.horizontal += int(number)
                sub.depth += int(number) * sub.aim
            case other:
                print("Unknown Instruction")
    print(sub)
    print(sub.depth * sub.horizontal)

if __name__ == '__main__':
    main()