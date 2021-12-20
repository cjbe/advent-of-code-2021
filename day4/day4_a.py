import numpy as np

def read_input(file):
    boards = []
    with open(file) as f:
        drawn_numbers = [int(x) for x in f.readline().split(",")]

        while f.readline():
            board = np.zeros((5,5))
            for i in range(5):
                nums = [int(x) for x in f.readline().split()]
                board[i] = nums
            boards.append(board)
    return drawn_numbers, boards

drawn_numbers, boards = read_input("day4.input")
boards_match = [np.zeros(boards[0].shape) for _ in boards]

def is_winner(board_match):
    for row in board_match:
        if np.all(row):
            return True
    for col in board_match.transpose():
        if np.all(col):
            return True
    return False

def run_game():
    for i, number in enumerate(drawn_numbers):
        for board, board_match in zip(boards, boards_match):
            board_match += (board == number)
            if is_winner(board_match):
                return number, board, board_match

if __name__ == "__main__":
    number, board, board_match = run_game()
    print(number, board)
    print(number * np.sum(board[board_match==0]))

