print("Hello ! Welcome To The Computer Quiz")

answer = input("Are you interested to play? ").lower()
if answer != "yes":
    quit()

print("Let's Play ")
score = 0

#question 1
answer = input("What is the expansion of CPU ? ").lower()
if answer == "central processing unit" :
    print ("Correct Answer!")
    score += 1
else :
    print("Wrong Answer.")

#question 2
answer = input("What is the expansion of GPU ? ").lower()
if answer == "graphics processing unit" :
    print ("Correct Answer!")
    score += 1
else :
    print("Wrong Answer.")

    #question 3
answer = input("What is the expansion of RAM ? ").lower()
if answer == "random access memory" :
    print ("Correct Answer!")
    score += 1
else :
    print("Wrong Answer.")

    #question 4
answer = input("What is the expansion of ROM ? ").lower()
if answer == "read only memory" :
    print ("Correct Answer!")
    score += 1
else :
    print("Wrong Answer.")

    #question 5
answer = input("What is the expansion of LAN ? ").lower()
if answer == "local area network" :
    print ("Correct Answer!")
    score += 1
else :
    print("Wrong Answer.")



print("\nYou answered  " + str(score) + " out of 5 questions  correctly" )

print("\nYou got" + str((score/5)*100) + "% " )

score_percentage = ((score/5)*100)
if (score_percentage >=60 ):
    print("Congratulations ! You are Qualified for next round ")
else :
    print("Sorry, you are not qualified. Please try again later.") 


#round2
print("Welcome to round 2")
answer = input("Are you interested to play? ").lower()
if answer != "yes":
    quit()

print("Let's Play ")
scoree = 0
   #question 1
answer = input("What is the expansion of WAN ? ").lower()
if answer == "wide area network" :
    print ("Correct Answer!")
    scoree += 1
else :
    print("Wrong Answer.")

   #question 2
answer = input("What is the expansion of DNS ? ").lower()
if answer == "domain name system" :
    print ("Correct Answer!")
    scoree += 1
else :
    print("Wrong Answer.")
   #question 3
answer = input("What is the expansion of IP ? ").lower()
if answer == "internet protocol" :
    print ("Correct Answer!")
    scoree += 1
else :
    print("Wrong Answer.")
   #question 4
answer = input("What is the expansion of HTML ? ").lower()
if answer == "hyper text markup language" :
    print ("Correct Answer!")
    scoree += 1
else :
    print("Wrong Answer.")
   #question 5
answer = input("What is the expansion of CSS ? ").lower()
if answer == "cascading stylesheet" :
    print ("Correct Answer!")
    scoree += 1
else :
    print("Wrong Answer.")
 

print("\nYou answered  " + str(scoree) + " out of 5 questions correctly" )


print("\nYou got" + str((scoree/5)*100) + "% " )


print("Completed")

scoree_percentage = ((scoree/5)*100)
 
total_score = score + scoree

print("your total score " , total_score)
