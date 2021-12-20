import numpy as np
from day4_a import read_input, is_winner

drawn_numbers, boards = read_input("day4.input")
boards_match = [np.zeros(boards[0].shape) for _ in boards]

def run_game():
    boards_completed = [False]*len(boards)
    for i, number in enumerate(drawn_numbers):
        for j, (board, completed, board_match) in enumerate(zip(boards, boards_completed, boards_match)):
            board_match += (board == number)
            if not completed and is_winner(board_match):
                boards_completed[j]=True
                if np.all(boards_completed):
                    return number, board, board_match

if __name__ == "__main__":
    number, board, board_match = run_game()
    print(number, board)
    print(number * np.sum(board[board_match==0]))
                