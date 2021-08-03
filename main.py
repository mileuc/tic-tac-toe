from os import system, name  # import only system from os
from time import sleep  # import sleep to show output for some time period
from art import game_title

# ----------------------------------------- CONSTANTS --------------------------------------------------------

GAME_ON = True
ROWS = 3
MAX_NUM_OF_TURNS = 9
WINNING_COMBOS = [(1, 4, 7), (1, 2, 3), (1, 5, 9), (2, 5, 8), (3, 6, 9), (4, 5, 6), (7, 8, 9), (3, 5, 7)]


# ----------------------------------------- CONSTANTS --------------------------------------------------------


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def print_board(board):
    print("\n")
    for row in range(1, ROWS + 1):
        if row < 3:
            print(f" {board[f'{(row * 3) - 2}']}" + " | "
                  + f"{board[f'{(row * 3) - 1}']}" + " | "
                  + f"{board[f'{(row * 3)}']}")
            print("---+---+---")
        else:
            print(f" {board[f'{(row * 3) - 2}']}" + " | "
                  + f"{board[f'{(row * 3) - 1}']}" + " | "
                  + f"{board[f'{(row * 3)}']}")

    print("\nPlayer 1: X")
    print("Player 2: O\n")


def update_board(board, space_number, player):
    # print(space_number)
    # print(board)
    if player == 1:
        board[f"{space_number}"] = 'X'
    else:
        board[f"{space_number}"] = 'O'


def check_end_of_game(board, player, turns):
    for combo in WINNING_COMBOS:
        if board[f"{combo[0]}"] == board[f"{combo[1]}"] == board[f"{combo[2]}"] != " ":
            print_board(board)
            print(f"Game over! Player {player} won!")
            return True

    if turns == MAX_NUM_OF_TURNS - 1:
        print("Game over! It's a draw!")
        return True


def play_game():
    legend = {"1": "1", "2": "2", "3": "3",
              "4": "4", "5": "5", "6": "6",
              "7": "7", "8": "8", "9": "9"}
    game_board = {"1": " ", "2": " ", "3": " ",
                  "4": " ", "5": " ", "6": " ",
                  "7": " ", "8": " ", "9": " "}
    print(f"{game_title}")
    print_board(legend)

    player_num = 1
    for turn in range(MAX_NUM_OF_TURNS):  # 0-8
        print_board(game_board)
        valid_number = False
        print(f"It's your turn, Player {player_num}!")
        while not valid_number:
            turn_input = input("Enter the number(1-9) of an empty spot on the board you want to take: ")
            try:
                if 0 < int(turn_input) <= 9:
                    if game_board[f"{turn_input}"] == " ":
                        valid_number = True
                        update_board(game_board, turn_input, player_num)
                        # if check_end_of_game(player_num, turn):
                        #     return True
                    else:
                        print("Sorry, that spot has already been taken! Please try again!")
                else:
                    print("The number you entered is not between 1-9! Please try again.")
            except ValueError:
                print("Invalid number entered. Please enter a valid number from 0-9.")

        if check_end_of_game(game_board, player_num, turn):
            return True
        if player_num % 2 != 0:
            player_num += 1
        else:
            player_num -= 1


# ----------------------------------------- MAIN CODE  --------------------------------------------------------


while GAME_ON:
    play_game()

    valid_response = False
    while not valid_response:
        clear_input = input("Do you want to play again? Enter y for Yes, or n for No: ").lower()
        if clear_input == "y":
            valid_response = True
            sleep(2)
            clear()
        elif clear_input == "n":
            print("Thanks for playing!")
            sleep(2)
            GAME_ON = False
            valid_response = True
        else:
            print("Invalid input, please try again.")
