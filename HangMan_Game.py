import random
#There is a list of fruits predefined list of words  
word_list = ["apple", "banana", "cherry", "grapes", "mango"]

#Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
 
#Initializing the Game state 
display = ['_'] * word_length
guessed_letters = []
lives = 6

#Game loop 
while lives > 0 and '_' in display:
    print("word to Guess:\n",' '.join(display))
    print("Guessed letters:",guessed_letters) 
    guess = input("Enter a letter :").lower()
    if not guess.isalpha() or len(guess)!= 1:
        print("Invalid input. Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You have already guessed the letter.")
        continue
    guessed_letters.append(guess)
    
    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
               display[i] = guess
        print("correct!")
    else:
        lives -= 1
        print(f"Incorrect! You have {lives} lives left.")


         # ========= * Game result * =========
if '_' not in display:
    print("Congratulations! You guessed the word:\n", chosen_word)
else:
    print("Game over. The word was:\n", chosen_word)
        
            
                
            
            
        
    
        
      