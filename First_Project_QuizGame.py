'''
#Les do this shi 

GIT CODES--> For Updates In Code
git add .
git commit -m "Describe what changed here"
git push




'''

print("Welcome to the game")
playing=input("Do You Want To Play? ")

if playing.lower() != "yes" :   #.lower() is used for  any BIG TEXT will converted to lower text & .upper
    quit()

  #1st QUE

score=0

print("Les Goo :), Good Luck I Guess")

answer=input("Short Form Of Central Processing Unit? ").lower()     #OR you can do that
if answer=="cpu":
    print("Correct!")
    score +=1
else:
    print("Incorrect! Answer is 'cpu' ")


#2nd Que

answer=input("Short Form Of Graphic Processing Unit? ")
if answer.lower()=="gpu":
    print("Correct!")
    score +=1
else:
    print("Incorrect! Answer is 'gpu' ")
    


#3rd Que

answer=input("Short Form Of Ramdom Acess Memory? ")
if answer.lower()=="ram":
    print("Correct!")
    score +=1
else:
    print("Incorrect! Answer is 'ram' ")

print("Your Score is:",score)
