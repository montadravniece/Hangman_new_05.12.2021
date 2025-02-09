class Game:
    """Summary of class - what is what.

    Provides building blocks of the Hangman game.

    Attributes:
    Typical usage example:

    """
    
    def __init__(self, word):
        """ 
        Performs operation X
        
        """
        self.word = word.upper()
        self.word_progress = list(len(word) * "-")
        self.lives = 6
        self.word_is_guessed = False
        self.guessed_letters = set()
        self.missed_letters = set()
        self.missed_words = set()
        self.user_name = input("Please, enter your name: ")
        

    def get_input(self):

# We input letters or words and delete if there is space we delete it with strip()
        guess = input("Please try and guess a letter: ").upper().strip()
        if len(guess) == 0:
            raise EOFError("Please, enter at least 1 character!")
        elif not guess.isalpha():
            raise TypeError("Please, use only letters!")

        return guess

    def play(self):
        while self.lives > 0 and self.word_is_guessed == False:
            self.print_status()
            
            try:
                guess = self.get_input()
            except (TypeError, EOFError) as err:
                print(err)
                continue

          
            if len(guess) == 1:

                if guess in self.guessed_letters or guess in self.missed_letters:
                    print("You already tried this letter\n")
                    continue
                
                if guess in self.word:
                    print("Correct you guessed a letter")
                    self.guessed_letters.add(guess)
                    # Open correctly guessed letter
                    for index, letter in enumerate(self.word):
                        if letter in self.guessed_letters:
                            self.word_progress[index] = letter
                    # Cheking if word is guessed
                    if self.word == ''.join(self.word_progress):
                        self.word_is_guessed = True
                else:
                    print("Wrong! Please try guessing another letter")
                    self.missed_letters.add(guess)   
                    self.lives -= 1       
            else:
                # If entered more than one simbol
                if len(guess) != len(self.word):
                    print("Word lenght in not correct try again\n")
                    continue
                
                if guess in self.missed_words:
                    print("You already tried this word\n")
                    continue
                    
                if self.word == guess:
                    self.word_is_guessed = True
                else:
                    print("Wrong word") 
                    self.missed_words.add(guess)
                    self.lives -= 1    
        
        self.print_game_over_message()
        
# Function that shows information to user            
    def print_status(self):
        print()
        self.draw_hangman()
        print(f"Word: {''.join(self.word_progress)}")
        print("Word leght:", len(self.word))
        print("Lives: ", self.lives * "♥")
        print(f"Missed letters: {', '.join(self.missed_letters)}")
        print(f"Missed words: {', '.join(self.missed_words)}")
        print()
        
    def print_game_over_message(self):

        print("\nGame over!")
        if self.word_is_guessed:
            print(" ░░░░░░░░░░░░░░░░░░░░▄████▄░░░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░░░░██░░░██░░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░░░▄█▀░░░░██░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░░▄█▀░░░░░██░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░██░░░░░░░██░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░▄█▀░░░░░░░░▀▀▀▀▀▀▀▀▀▀▀██▄\n",
            "▄███████████████▀░░░░░░░░░░░░░░░░░░░░░██\n",
            "██░░░░░░░░░░█▀░░░░░░░░░░░░░░░░░░░░░░▄▄█▀\n",
            "██░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░██░\n",
            "██░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░▄██░\n",
            "██░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░▀█░░\n",
            "██░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░▄█░░\n",
            "██░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░███░░\n",
            "██░░░░░░░░░░█▄░░░░░░░░░░░░░░░░░░░░░▄█▀░░\n",
            "██░░░░░░░░░░████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██▀░░░\n",
            "▀████████████▀░░░▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀░░░░░░░\n")            
            print(f"Congrats {self.user_name} You WON! Word: {self.word}")
            
        else:
            print(
                "     ______  \n",
                "   |      0  \n",
                "   |     /█\ \n",
                "   |      █  \n",
                "   |     / \ \n",
                "___________\n"
            )

            print(f"You Lost {self.user_name}! Correct word: {self.word}")
    
    # Pictures of hangman            
    def draw_hangman(self):
        if self.lives == 6:
            print(
                "           \n",
                "           \n",
                "           \n",
                "           \n",
                "           \n",
                "___________\n"
            )
      
        elif self.lives == 5:
            print(
                "    _      \n",
                "   |       \n",
                "   |       \n",
                "   |       \n",
                "   |       \n",
                "___________\n"
            )
        elif self.lives == 4:
            print(
                "     ______  \n",
                "   |       \n",
                "   |       \n",
                "   |       \n",
                "   |       \n",
                "___________\n"
            )
        elif self.lives == 3:
            print(
                "     ______  \n",
                "   |      0  \n",
                "   |       \n",
                "   |       \n",
                "   |       \n",
                "___________\n"
            )
        elif self.lives == 2:
            print(
                "     ______  \n",
                "   |      0  \n",
                "   |      █  \n",
                "   |      █  \n",
                "   |       \n",
                "___________\n"
            )
        elif self.lives == 1:
            print(
                "     ______  \n",
                "   |      0  \n",
                "   |     /█\ \n",
                "   |      █  \n",
                "   |       \n",
                "___________\n"
            )
