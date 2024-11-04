import random
import json

score = 0

def player_1():
    while True:
        player_in = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors or Q to quit: ").lower()
        if player_in == "1":
            return 1
        elif player_in == "2":
            return 2
        elif player_in == "3":
            return 3
        elif player_in == "q":
            exit()
        else:
            print("Wrong number. Try again.")


def player_2():
    pass


def computer():
    rand_number = random.randint(1, 3)
    #print(f"Computer playes {}")
    return rand_number


def check_win():
    if player_1() == computer():
        print("You win!")
    pass

def check_loss():
    pass


def check_draw():
    if player_1() == computer():
        print("Draw!")


def convert_num_to_word(num):
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "scissors"
    

def board():
    print("##################################################")
    print("########## Rock, Paper, Scissors Report ##########")
    print("##################################################")
    print(f"-" * 50)
    print("| Round | User Played | Computer Played | Outcome |")
    print(f"-" * 50)
    print(f"|     1|             |                 |         |")
    print(f"-" * 50)
    print(f"|     2|             |                 |         |")
    print(f"-" * 50)
    print(f"|     3|             |                 |         |")
    print(f"-" * 50)
    print(f"|     4|             |                 |         |")
    print(f"-" * 50)
    print(f"|     5|             |                 |         |")
    print(f"-" * 50)
    pass


def round_handler(round, records) -> None:
    print(f"{round}")
    p = player_1()
    c = computer()
    records[round]["user"] =p
    records[round]["comp"] = c
    outcome = determine_outcome(p, c)
    records[round]["outcome"] = outcome


def determine_outcome(player_move, computer_move):
    #return win, lose, tie
    pass

def main():
    game_mem = {"Round 1":{},"Round 2":{},"Round 3":{},"Round 4":{},"Round 5":{}}
    for entry in game_mem.keys():
        round_handler(entry, game_mem)

    print(json.dumps(game_mem, indent=4))

if __name__ == "__main__":
    main()