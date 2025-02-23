import time
import random

break_duration = 1  # Adds a little pause so the game is not rushed
league_table = {}   # Creates a dictionary with all players' names

def display_league_table():  # The basis for the League Table
    print("\nLEAGUE TABLE:")
    for player, score in sorted(league_table.items(), key=lambda x: x[1], reverse=True):
        print(f"{player}: {score}")  # Prints the Player name and Score

def existing_or_new_player():
    while True:
        choice = input("Would you like to play as an existing player or a new player? (existing/new): ").lower()
        if choice in ['existing', 'new']:
            return choice  # Having the choice function simplifies it a bit
        else:
            print("Invalid choice. Please enter 'existing' or 'new'.")

while True:
    player_choice = existing_or_new_player()

    if player_choice == 'existing':  # Makes sure that the player exists
        name = input("Enter your name: ")
        if name not in league_table:
            print("Player not found. Starting as a new player.")
            player_choice = 'new'

    if player_choice == 'new':
        name = input("What would you like to be called?")

    time.sleep(break_duration)  # Puts a 1-second break so it's not too fast

    print(f"Let's begin, {name}!")

    time.sleep(break_duration)

    score = 0   # Score starts at 0, as it should
    tries = 3   # The number of attempts you have is 3  

    with open('Questions.txt', 'r') as file:  # Reads my text file with the definitions
        lines = file.readlines()

    items_data = []  # This is pulling the data from my file in the correct format, as there are 3 possible answers
    for line in lines:
        items, description = line.strip().split("=")
        items_data.append((items.split(","), description))

    asked_questions = []  # Makes the used questions a different list

    for _ in range(6):  # Asking 6 questions and getting a random set of items that hasn't been asked to that user yet
        remaining_items = list(set(range(len(items_data))) - set(asked_questions))
        random_index = random.choice(remaining_items)
        random_items, item_description = items_data[random_index]

        print(f"\nI am . . . {item_description}")

        out_of_tries = False  # If they have tries, the game continues
        while tries > 0:
            answer = input(f"Guess the name of this item: ")
            if answer in random_items:
                print("You're Correct!")
                score += 1
                break   # Break out of the current question loop if the answer is correct
            else:
                tries -= 1
                print(f"You're Incorrect! You have {tries} tries left.")
                if tries == 0:
                    print(f"You've run out of tries. The correct answers were {', '.join(random_items)}.")
                    out_of_tries = True
                    break

        if out_of_tries:   # If the user is out of tries, the game ends
            break
        asked_questions.append(random_index)

        if _ < 5:   # Pause for a break between questions
            print(f"\nNext Question in {break_duration} seconds...")
            time.sleep(break_duration)

    print(f"Well done, {name}! Your final score is: {score}/6")
    league_table[name] = score  # This updates the league table with the player's score

    display_league_table()  # This displays the League Table to the player

    play_again = input("Do you want to play again? (yes/no) ").lower()
    
    while True:
        if play_again == "no":
            print("Goodbye")
            break
        elif play_again == "yes":
            # This will be executed if the user enters "yes"
            print("Let's play again!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            play_again = input("Do you want to play again? (yes/no) ").lower()

    if play_again == "no":
        break  # This breaks out of the outer loop 
