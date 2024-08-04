print("Welcome to Trivia Titan, answer questions and expand your knowledge!")
answer = input("Do you want to play? ").strip().lower()

# List of accepted positive responses
positive_responses = ["yes", "y", "yeah", "sure", "okay", "ok", "of course", "absolutely", "ya", "yep"]

if answer not in positive_responses:
    quit()

print("Great! Let's start the game.")


answer = input("Which is the tallest building in the world? ") 
#list of accepted answers 
accepted_answers = ["burj khalifa" , "Burj khalifa" , "Burj Khalifa"]
if answer in accepted_answers:
    print("correct! +1 point ")
else: 
    print("incorrect! - 1 point ")  

print("okay! lets proceed to question 2! ")
answer = input("on which cities did the atomic bomb get released? ") 
#List of accpeted_answers 
accpeted_answers = ["nagasaki and hiroshima" , "Nagasaki and Hiroshima", "nagasaki and Hiroshima", "Nagasaki and hiroshima"]

if answer in accpeted_answers: 
    print("correct! +1 point ")
else:
    print("incorrect! - 1 point ") 
print("lets move to question 3! ")
answer = input("How many continents are there on Earth? ").strip()

# List of accepted answers
accepted_answers = ["7", "7 continents"]

if answer in accepted_answers:
    print("Correct, +1 point! ")
    
else:
    print("incorrect! - 1 point ") 
print("if you got all 3/3 questions correct then you have achieved 3 points and you proceed to the next level! ")
print("lets begin with the first question of level 2! ")
answer = input("What is the capital of pakistan? ")
#List of accepted answers 
accepted_answers = ["islamabad" , "Islamabad"]

if answer in accepted_answers:
    print("correct! + 1 point ")
else:
    print("incorrect! -1 point ") 
print("lets move on to question 2! ")
answer = input("In which country is the holiest place for muslims located? ")
#List of accepted answers 
accepted_answers = ["mecca" , "Mecca"]

if answer in accepted_answers: 
    print("correct! + 1 point ")
else: 
    print("incorrect! - 1 point ") 
print("lets move on to question 3! ")
answer = input("Who was accused for the crime of 9/11? ")
#list of accepted answers 
accepted_answers = ["osama bin laden" , "Osama bin laden"]

if answer in accepted_answers: 
    print("correct! +1 point ")
else:
    print("incorrect! -1 point ") 
print("Let's move on to question 4!")
answer = input("Who is the most famous athlete in the world? ").strip().lower()

# List of accepted answers
accepted_answers = ["cristiano ronaldo", "ronaldo", "cr7"]

if answer in accepted_answers:
    print("Correct! +1 point")
else:
    print("Incorrect! -1 point")
print("lets move to the final question of level 2! ")
answer = input("Which is the largest country in Asia ")
#list of accepted answers
accepted_answers = ("russia" , "Russia")
if answer in accepted_answers: 
    print("correct! +1 point ")
else: 
    print ("incorrect! - 1 point ") 
print("Okay! Now that we are done with level 2, level 3 is going to be the second last level! The general knowledge you have will be based on the amount of points you get in the next level. Good luck!")


answer = input("What is the smallest country in the world by land area? ") 
#List of accepted_answers 

accepted_answers = ["Vatican city", "vatican city", "Vatican City"]

if answer in accepted_answers:
    print("correct, +1 point. ") 
else:
    print("incorrect! - 1 point ")

print("Attempt question 2. ")
answer = input("In which year did the titanic sink? ")
#List of accepted answers

accepted_answers = ["1912"]
if answer in accepted_answers: 
    print("correct, +5 points. ")
else:
    print("incorrect, -5 points. ")
print("attempt question 3. ")
answer = input("Which planet has the most moons in our solar system? ")
#List of accepted answers 

accepted_answers = ["saturn", "Saturn"]
if answer in accpeted_answers: 
    print("correct, +5 points. ")
else: 
    print("incorrect, -5 points. ")
print("Attempt question 4. ")
answer = input("Which is the capital city of Australia? ").strip()

# List of accepted answers
accepted_answers = ["canberra", "Canberra"]

if answer in accepted_answers:
    print("Correct, +5 points.")
else:
    print("Incorrect! -5 points. ")

print("Attempt question 5.") 
answer = input("Which is the longest river in the world? ")
#List of accepted answers 
accepted_answers = ["river nile", "nile river", "River Nile", "River nile", "river Nile", "Nile", "nile"]
if answer in accpeted_answers: 
    print("correct, +5 points. ")
else:
    print("incorrect, -5 points. ")
print("Attempt question 6. ")
answer = input("Who assasinated Abraham lincon? ")
#List of accpeted_answers 
accpeted_answers =["john booth", "John Booth","John booth", "john Booth", "John wilkes booth","John Wilkes Booth","john wilkes booth"]
if answer in accepted_answers: 
    print("correct, +5 points. ")
else: 
    print("incorrect, -5 points. ")
print("We are done with all the levels of Trivia Titan, if you managed to get 25-30 points, you have good general knowledge, if you got 15-20 points then you have middle class general knowledge and if you got 5-10 points, improve your general knowlege. We will play next time. ")





