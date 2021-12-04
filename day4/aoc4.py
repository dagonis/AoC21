from dataclasses import dataclass

@dataclass
class Number:
    val: int
    marked: bool

@dataclass
class Board:
    raw_numbers: list
    won: bool = False

    def __post_init__(self):
        numbers = []
        for row in self.raw_numbers:
            for number in row.split():
                numbers.append(Number(number, False))
        self.numbers = numbers
        self.rows = []
        self.columns = []
        for n in range(0,25,5):
            self.rows.append(numbers[n:n+5])
        for n in range(0,5):
            self.columns.append(numbers[n::5])

    
    def check_for_win(self) -> bool:
        for row in self.rows:
            row_win = 0
            for number in row:
                if number.marked:
                    row_win += 1
                    if row_win == 5:
                        return True
        for column in self.columns:
            col_win = 0
            for number in column:
                if number.marked:
                    col_win += 1
                    if col_win == 5:
                        return True
        return False
    
    def sum_unmarked_numbers(self):
        out_sum = 0
        for number in self.numbers:
            if not number.marked:
                out_sum += int(number.val)
        return out_sum
            

def main() -> None:
    with open('input.txt', 'r') as input_file:
        lines = [_.strip() for _ in input_file]
    calls = lines[0].split(',')
    while '' in lines:
        lines.remove('')
    raw_boards = []
    for n in range(0, len(lines)-1, 5):
        raw_boards.append(lines[1:][n:n+5])
    boards = []
    for raw_board in raw_boards:
        boards.append(Board(raw_board))
    winning_board = None
    last_call = 0
    won = False
    ##########
    # Part 1 #
    ##########
    for call in calls:
        if not won:
            for board in boards:
                for number in board.numbers:
                    if call == number.val:
                        number.marked = True
                        if board.check_for_win():
                            winning_board = board
                            last_call = call
                            won = True
                            break
                        else:
                            pass
                    else:
                        pass
    print(winning_board.sum_unmarked_numbers() * int(last_call))
    ##########
    # Part 2 #
    ##########
    winning_boards = []
    for call in calls:
        for board in boards:
            if board.won:
                pass
            else:
                for number in board.numbers:
                    if call == number.val:
                        number.marked = True
                        if board.check_for_win():
                            board.won = True
                            winning_boards.append(board)
                            last_call = call
    print(winning_boards[-1].sum_unmarked_numbers() * int(last_call))


if __name__ == '__main__':
    main()