print("Welcome to the Football Quiz Game!")

playing = input("Do you want to play the game? ")

# if playing.lower() not in ["YES","Y","y","yes"]:
if playing.lower() != "YES"
    quit()
else:
    print("LETSSSS GOOOOOOO")

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

answer = input("Which is the best club of the world? ")
if answer == "barca":
    print("Correct!")
else:
    print("Incorrect!")
    
answer = input("Which club won sextuple? ")
if answer == "barcelona":
    print("Correct!")
else:
    print("Incorrect!")
    
answer = input("Best striker of this generation? ")
if answer == "suarez":
    print("Correct!")
else:
    print("Incorrect!")
    
answer = input("3rd best player after Messi and Ronaldo? ")
if answer == "neymar":
    print("Correct!")
else:
    print("Incorrect!")
    
