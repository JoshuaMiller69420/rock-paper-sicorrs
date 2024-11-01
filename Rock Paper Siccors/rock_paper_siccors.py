import random
score = 0

def player():
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


def user_2():
    pass

def convert_num_to_word(num):
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "scissors"

def computer():
    rand_number = random.randint(0, 3)
    return rand_number


def check_win():
    if  ==


def round_handler() -> None:
    round = 0
    print(f"Round {round + 1}")
    player_move = player()



def main():
    round_handler()

if __name__ == "__main__":
    main()