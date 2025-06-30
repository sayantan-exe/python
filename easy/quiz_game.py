print("Welcome to the Football Quiz Game!")

playing = input("Do you want to play the game? ")

# if playing.lower() not in ["YES","Y","y","yes"]:
if playing.lower() != "yes":
    quit()
else:
    print("LETSSSS GOOOOOOO")
    score=0
    correct=0
    incorrect=0

# answer = input("Who is GOAT of football? ")
# attempts = 0
# while attempts<=3:
#     if answer == "MESSI":
#         print('Correct!')
#         break
#     else:
#         attempts += 1
#         if attempts < 3:
#             print("INCORRECT !!")
#             input("Try again ")
#         else:
#             print("GAME OVER")
#             quit()

answer = input("Which is the best club of the world? ").lower()
if answer == "barca":
    print("Correct!")
    score += 1
    correct += 1
else:
    print("Incorrect!")
    score -= 1
    incorrect += 1
    
answer = input("Which club won sextuple? ").lower()
if answer == "barcelona":
    print("Correct!")
    score += 1
    correct += 1
else:
    print("Incorrect!")
    score -= 1
    incorrect += 1
    
answer = input("Best striker of this generation? ").lower()
if answer == "suarez":
    print("Correct!")
    score += 1
    correct += 1
else:
    print("Incorrect!")
    score -= 1
    incorrect += 1
    
answer = input("3rd best player after Messi and Ronaldo? ").lower()
if answer == "neymar":
    print("Correct!")
    score += 1
    correct += 1
else:
    print("Incorrect!")
    score -= 1
    incorrect += 1
    
if correct>0 and incorrect>0:    
    print(f"You got {correct} questions correct and {incorrect} questions incorrect.")
elif correct==0:
    print(f"You got {incorrect} questions incorrect.")
else:
    print(f"You got {correct} questions correct.")
    
