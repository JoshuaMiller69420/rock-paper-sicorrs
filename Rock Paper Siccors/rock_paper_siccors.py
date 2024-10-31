import random
score = 0

def user_1(score):
    user_in = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors or Q to quit: ").lower()
    if user_in == "1":
        return "rock"
        score += 1
    elif user_in == "2":
        return "paper"
        score += 1
    elif user_1 == "3":
        return "scissors"
        score += 1
    elif user_1 == "q":
        exit()
    else:
        print("Wrong number. Try again.")


def compu_in():
    rand_number = random.randint(0, 3)
    return

def user_2():
    pass


def round_handler() -> None:
    
    print(current_round)
    user_1()


def score_counter() -> None:
    pass


def main() -> None:
    print("""
     _____            _      _____                         _____      _                        
    |  __ \\          | |    |  __ \\                       / ____|    (_)                       
    | |__) |___   ___| | __ | |__) |_ _ _ __   ___ _ __  | (___   ___ _ ___ ___  ___  _ __ ___ 
    |  _  // _ \\ / __| |/ / |  ___/ _` | '_ \\ / _ \\ '__|  \\___ \\ / __| / __/ __|/ _ \\| '__/ __|
    | | \\ \\ (_) | (__|   <  | |  | (_| | |_) |  __/ |     ____) | (__| \\__ \\__ \\ (_) | |  \\__ \\
    |_|  \\_\\___/ \\___|_|\\_\\ |_|   \\__,_| .__/ \\___|_|    |_____/ \\___|_|___/___/\\___/|_|  |___/
                                       | |                                                     
                                       |_|     
        _______           _______               _______ 
    ---'   ____)      ---'   ____)____     ---'    ____)____ 
          (_____)               ______)               ______) 
          (_____)               _______)           __________) 
          (____)               _______)           (____) 
    ---.__(___)       ---.__________)      ---.__(___)""")
    round_handler()

if __name__ == "__main__":
    main()