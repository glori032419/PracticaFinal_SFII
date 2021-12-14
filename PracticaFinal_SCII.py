import random
print("\t\tWelcome to the Guess My Word App")
game_dict = {'sports':['cycling', 'swimming', 'football', 'tennis', 'basketball', 'badminton' ] ,'colors':['red', 'orange', 'yellow', 'green', 'blue', 'purple'] ,'fruits':['apple', 'orange', 'lemon', 'cherry', 'pear', 'kiwi'] ,'classes':['history', 'language', 'math', 'science', 'english', 'french']}
game_keys = []

for keys in game_dict:
    game_keys.append(keys)
comprobante = True

while comprobante:
    game_category = random.choice(game_keys)
    game_word = game_dict[game_category][random.randint(0,5)]
    blank_word = []
    for i in range(len(game_word)):
        blank_word.append("-")
    blank_word2 = "".join(blank_word) 
    #guess = ""
    guess_count = 0
    print("Guess a ",len(game_word) ," letter word from the following category:",game_category)
    print(blank_word2)
    guess = input("\nEnter your guess: ")
    guess_count += 1
    
    while True:
        if guess != game_word:          
            letter_count = random.randint(0,len(blank_word))     
            for letra in game_word:
                if letra in guess:
                    print(letra,end="")
                else:
                    print("-", end="")
                    guess_count+=1
            print("\nThat is not correct. Let us reveal a letter to help you!")
            guess = input("\nEnter your guess: ")
        elif guess == game_word:
    
            print("Correct! You guessed the word in ",guess_count ," guesses.")
            break
            
            
    c = input("Would you like to play again (y/n): ").lower()
    if c == "y":
        continue
    elif c == "n":
        print("\nThank you for playing our game.")
        band = False
