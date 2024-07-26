import random

print('''Let's play a game of Luck.
In this game, you have to choose a number between 1 to 50 and the computer will also choose a number. If your number is greater than the computer's number, you will win; otherwise, the computer wins.

-----------------------------------⚠️ ALERT ⚠️ -------------------------------
Make sure to enter a number between 1 and 50.
''')

def game():
    # Generate a random number between 1 and 50 for the computer
    comp = random.randint(1, 62)
    # Prompt user to enter a number
    user = int(input("Enter a number between 1 and 50: "))

    # Check if the user's number is within the valid range
    if user > 50 or user < 1:
        print("Please enter a number between 1 and 50.")
        return  # Exit the function if the number is out of range

    # Compare user's number with the computer's number
    if user > comp:
        print(f"Congratulations! You won. Your number: {user}, Computer's number: {comp}")
        hiscore = user
    else:
        print(f"Sorry, you lost. Your number: {user}, Computer's number: {comp}")
        hiscore = 0

    # Write the high score to the file if user wins
    with open("hiscore.txt", "a") as f:
        f.write(f"User number: {user}, Computer number: {comp}, High score: {hiscore}\n")

# Call the game function to start the game
game()
