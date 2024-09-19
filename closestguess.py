import random



random_number = random.randint(50, 1000)


# well atleast something's are easy
while True:
    number_of_players = input("Enter the number of players: ")

    if number_of_players.isdigit():
        number_of_players = int(number_of_players)
        if number_of_players < 2:
            print("Enter a number greater than 1!")
            number_of_players = input("Enter the number of players: ")
            continue
        else:
            break
    else:
        print("Enter a valid number!")
        number_of_players = input("Enter the number of players: ")
        continue

# the trash part is coming up
# i will probably waste 30-40 minutes writting this
# because i am "dumb" enough to not use chatGPT
# or any other AI to write this for me
# well thanks to github premium i do have github copilot
# but i am not using it because i am "dumb"
# well here comes the trash part



# creating arrays for players and their scores
players = [input(f"Enter the name of player {i+1}: ") for i in range(number_of_players)]    # creates the array with name so that I can use it later to output it with the name.. Hope it works though
players_guess = [0 for _ in range(number_of_players)]      # this creates an array which would contain their guess and the guess closest to the guessed number will win

print("\n\n")




# loop to get the guess from the players
max_number_of_loops = len(players)  # this is the number of times the loop will run
current_loop = 0    # this is the current loop number
while current_loop < max_number_of_loops:   # this loop will run until the number of players have guessed the number
    for player_idx in range(number_of_players):   # this loop will run for each player 
        print(f"{players[player_idx]}'s turn")  # this will print the name of the player whose turn it is

        while True:
            guess = input(f"Enter your guess {players[player_idx]}: ")  # this will take the input from the player
            
            if guess.isdigit():
                guess = int(guess)  # this will convert the input to integer
                if guess < 50 or guess > 1000:  # this will check if the input is between 50 and 1000
                    print("Enter a number between 50 and 1000!")    # if the input is not between 50 and 1000 then it will print this message
                    continue
                else:
                    players_guess[player_idx] += guess  # this will add the guess to the player's score    
                    print("\n")
                    break
            else:
                print("Enter a valid number!")
                continue
        current_loop += 1


# finding the closest guess
closest_guess = 0
closest_guess_idx = 0
for idx, guess in enumerate(players_guess):
    if abs(random_number - guess) < abs(random_number - closest_guess):     # I don't know how the heck I managed to write this piece of randomness.
        closest_guess = guess                                               # who knew that mod can be used here as well :)
        closest_guess_idx = idx


print("\n\n")
print(f"The number was {random_number}")
print(f"The closest guess is {closest_guess} by {players[closest_guess_idx]}")

