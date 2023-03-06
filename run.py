

#-----------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num +=1

    display_score(correct_guesses, guesses)
#-----------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else: 
        print("WRONG!")
        return 0
#-----------------------
def display_score(correct_guesses, guesses):
    print("-----------------------")
    print("Results")
    print("-----------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print((i), end="")
    print()
#-----------------------
def play_again():
    pass
#-----------------------

# dictionary created for the questions

questions = {
    "What percentage of the Earth's surface is covered by Oceans?: ": "A",
    "What is the percentage of the planet's oceans that have been explored? ": "A",
    "Which one the following islands is not in the Atlantic Ocean? ": "C",
    "Which of the following oceans is the smallest and the shallowest? ": "D",
    "The Pacific is home to the deepest known trench on the planet - what's its name? ": "A"
}

options = [["A. 20%", "B. 40%","C. 50%","D. 70%"],
           ["A. 5%", "B. 25%", "C. 50%", "D. 75%"],
           ["A. The Bahanmas", "B. Azores", "C, Madagascar", "D, Canarary Islands"],
           ["A, Atlantic", "B. Pacific", "C. Indian", "D. Arctic"],
           ["A. Mariana Trench", "B. Kermadec Trench", "C. South Sandwich Trench", "D. Izu-Ogasawara Trench"]]

new_game()
