'''
#Les do this shi 


git add First_Project_QuizGame.py   /   git add README.md
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

answer=input("What Is CPU? ").lower()     #OR you can do that
if answer=="Central Processing Unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect! Answer is 'Central Processing Unit' ")


#2nd Que

answer=input("What Is  GPU? ")
if answer.lower()=="Graphic Processing Unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect! Answer is 'Graphic Processing Unit' ")
    


#3rd Que

answer=input("What is the output of print(type(5)) :  (a)5 (b)<class 'int'> (c)int (d)Error ")
if answer.lower()=="b":
    print("Correct!")
    score +=1
else:
    print("Incorrect! Answer is '(b):<class 'int'>' ")


answer=input("What keyword is used to create a function in Python? : (a) func (b) function (c) def (d) lambda ")
if answer.lower()=="c":
    print("Correct!")
    score +=1
else:
    print("Incorrect! Answer is '(c):def' ")


answer=input("What will print(2 ** 3 ** 2) output? : (a) 64 (b) 512 (c) 256 (d) Error ")
if answer.lower()=="a":
    print("Correct!")
    score +=1
else:
    print("Incorrect! Answer is '(a):64' ")





#can use print("You got " + str(score) + "Questions Correct!")
print("Your Score is:",score)       
#OR print("{:.0f}%".format(score/3*100)) 
#OR print(str(score/3*100))


