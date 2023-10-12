#Game 2
# ----------------------------
def new_game():

     guesses =[]
     correct_guesses = 0
     question_num=1

     for key in questions:
         print("----------------------------")
         print(key)
         for i in options[question_num -1]:
             print(i)
         guess=input("Enter your choice( A, B, C or D):  ").upper()
         guesses.append(guess)
         correct_guesses += check_answers(questions.get(key), guess)
         question_num +=1

         display_score(correct_guesses, guesses)
# ----------------------------
def check_answers(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("That's incorrect!")
        return 0

# ----------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------")
    print("RESULTS")
    def play_again():
     pass
# ----------------------------
#Below is a dictionary
questions = { "Who created python?: ": "A",
              "When was Python created?: ": "B",
              "Python is distributed to which comedy group?: ": "C",
              "Is the earth round?: ": "A"}
#Below is a 2D list
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zukerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python","D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's earth?"]]

new_game()
