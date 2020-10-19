#QUIZ TIME YES
print("Welcome to this amazing quiz ok")
print("You will answer 5 Questions")
print("Question 1")
answer1 = input("What does the Twitch term poggers mean?")
answer1 = answer1.title()
counter = 1
while answer1 != "Good":
    answer1 = input("Incorrect, try again.")
    answer1 = answer1.title()
    counter = counter + 1
print("WOW, you got it right! You had",counter, "attempts")

print("Question 2")
answer2 = input("What is the halloween film that Adam Sandler made with Netflix that is very terrible.")
answer2 = answer2.title()
counter = 1
while answer2 != "Hubie Halloween":
    answer2 = input("Incorrect, try again.")
    answer2 = answer2.title()
    counter = counter +1
print("WOW, you got it right! You had",counter, "attempts")

print("Question 3")
answer3 = input("Who tried to kill Carole Baskin?")
answer3 = answer3.title()
counter = 1
while answer3 != "Joe Exotic":
    answer3 = input("Incorrect, try again.")
    answer3 = answer3.title()
    counter = counter +1
print("WOW, you got it right! You had",counter, "attempts")

print("Question 4")
answer4 = input("What is the most popular series on Netflix")
answer4 = answer4.title()
counter = 1
while answer4 != "Stranger Things":
    answer4 = input("Incorrect, try again.")
    answer4 = answer4.title()
    counter = counter +1
print("WOW, you got it right! You had",counter, "attempts")

print("Question 5")
answer5 = input("Who is the annoying TikTok dancer who has the most followers")
answer5 = answer5.title()
counter = 1
while answer5 != "Charli D'Amelio":
    answer5 = input("Incorrect, try again.")
    answer5 = answer5.title()
    counter = counter +1
print("WOW, you got it right! You had",counter, "attempts")
