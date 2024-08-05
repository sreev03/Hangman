# Hangman With Python

import random

countries_pool = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua", "Argentina", "Armenia", 
"Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", 
"Benin", "Bhutan", "Bolivia", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burundi", "Cambodia", "Cameroon", "Canada", 
"Chile", "China", "Colombia", "Comoros", "Croatia", "Cuba", "Cyprus", "Denmark", "Djibouti", "Dominica", "Ecuador", 
"Egypt", "El Salvador", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", 
"Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guyana", "Haiti", "Honduras", "Hungary", 
"Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", 
"Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", 
"Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Mauritania", "Mauritius", 
"Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nauru", "Nepal", "Netherlands", 
"Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Paraguay", "Peru", "Philippines", "Poland", 
"Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Samoa", "Senegal", "Serbia", "Seychelles", "Singapore", "Slovakia", 
"Slovenia", "Somalia", "Spain", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", 
"Thailand", "Togo", "Tonga", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "Uruguay", "Uzbekistan", 
"Vanuatu", "Vatican", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]   # this is a list containing all the words for the game

while True:
    
    word = random.choice(countries_pool).upper()    # this is the word that the player would be guessing

    guess_count = 5    # this is the number of incorrects guesses allowed

    wrong_guesses = []    # this is to store the letters guessed by the player but are not in the word

    correct_guess = ['_'] * len(word)    # this is what the player has guessed so far

    print("Welcome To Hangman! \n")

    # display the instructions on how to play the game
    print('Your goal is to guess the randomly chosen country.\nThe catch here is that you are allowed only 5 wrong guesses.\nIf you run out of guesses, the game ends.\nKeep playing to guess more countries and have fun!')

    print('\nGuess the Country: ',' '.join(correct_guess),'\n')
    
    while guess_count > 0 and ''.join(correct_guess) != word:

        guess = input("\nPlease enter your guess!(enter a single letter only : for example, A) ").upper()    # collect player's guess

        if len(guess) != 1 or guess.isalpha() is False:    # incase the player had entered more than one character or an invalid character
            print(" Please enter a valid input ")
            continue

        if guess in word:    # when the player's guess is correct
            for index, letter in enumerate(word):
                if letter == guess:
                    correct_guess[index] = guess    # fill in the correct guess at the right places
            print("Great Guess! :)")

        else:
            if guess not in wrong_guesses:
                wrong_guesses.append(guess)
                guess_count -=1    # update the number of wrong guesses remaining
            print(f"Opps :(\nA bad guess. You have {guess_count} wrong guesses left.")

        print("".join(correct_guess),f'\nWrong guess: {','.join(wrong_guesses)}\n')
    
    if ''.join(correct_guess) == word:
        print(f'Congratulations! You won! The word was {word}.\n')
    
    else:
        print(f'Oops! Ran out of guesses. The word was {word}.\n')

    play_again = input("Do you want to play again? (yes/no): ").upper()     
    
    if play_again != 'YES':    # if the player doesn't want to continue the game
        # exit the program
        break
