import random

names = ["Prateek", "Anshul", "Goutham", "Karun", "Monil"] #array of monsters
used_names = [] #array for adding monsters already used

len_names = len(names) #length of the array of monsters

def generateRandomNumber (num1, num2):

    if num2 == -1:
        win_game()

    return random.randint(num1, num2) #will generate random number inclusive of 2nd

#function that will need to be called each new round
def pick_a_name():
    #will generate random monster from array
    global len_names #refers to the global len_names variable
    random_num = generateRandomNumber(0, len_names - 1)

    monster = names[random_num] #stores the name of the monster

    #remove monster name and add to used list
    names.remove(monster)
    used_names.append(monster)

    len_names -= 1 #reduces len_names by 1
    return monster

#this function will run at the start of the game. Will call new_round() function
def start():
    print "Welcome to the game"
    print "This is a text-based adventure game"
    print "Your task is to get past each monster"
    print "\n"
    print "You will be required to provide yes or no answers"
    print "Choose wisely"

    print "Are you ready to get started?",
    print "Type y or n"
    command = user_input("y", "n") # accept input for whether to start the game or not

    #initializing a round variable here to pass to the next_round function
    round = 1
    if(command == "y"):
        next_round(round)
    if(command == "n"):
        quit_game()

#this function will take the user to a new round
def next_round(round):

    monster = pick_a_name() #variable to store monster name
    print ""
    print "Welcome to round %d" % round
    print "Meet your monster,",
    print "%s" % monster
    print ""

    print "Here is the challenge for this monster"
    monster_challenge(monster)
    round += 1 #adding 1 to the round
    next_round(round)

#this function will end the game for the user
def quit_game():
    print "Thank you for playing"
    print "Goodbye!"
    exit(0)

#function to generate monster challenges
def monster_challenge(monster):
    if monster == "Goutham":
        goutham_challenge() #calling monster specific challenge here
        return
    elif monster == "Prateek":
        prateek_challenge()
        return
    elif monster == "Karun":
        karun_challenge()
        return
    elif monster == "Anshul":
        anshul_challenge()
        return
    elif monster == "Monil":
        monil_challenge()
        return

def goutham_challenge():
    print "Are you a woman?"
    command = user_input("y", "n")
    if command == "y": #if user is a woman
        goutham_balls = generateRandomNumber(0, 1) #variable to check balls of goutham
        if goutham_balls > 0.5: #if goutham hits on woman
            print "You're in luck, Goutham will now make a move on you"
            print "Goutham says: So what major are you in?"
            print "Did this move turn you on?"
            command = user_input("y", "n")

            if command == "y": #if woman user loses
                print ""
                print "Dear god, you have no taste! I am booting you out!"
                quit_game()
            else: #if woman user wins
                print ""
                print "Congrats! You progress to the next round"
                return
        elif goutham_balls <= 0.5: #if goutham does not hit on woman
            print "Goutham doesn't find you attractive"
            print "You can safely move on to the next round"
            return
    elif command == "n": #if user is a guy
        print "Goutham says: Okay, can you buy me a drink?"
        print "What do you do? Type y or n"
        command = user_input("y", "n")
        if command == "y": #if user buys goutham a drink
            print "Congrats, you now have a leech!"
            print "You go broke and die!"
            quit_game()
        elif command == "n": #if user does not buy goutham a drink
            print "Good for you! Go on to the next round"
            return

#Prateek's Challenge
def prateek_challenge():

    #giant print block
    print "The challenge for Prateek will not be straightforward"
    print "Mostly because Prateek is not straightforward"
    print "We will now need a why not? factor"
    print "The why not factor will be based on blind luck"
    print "Guess a random number and if it matches random generation"
    print "Enter any number between 1 and 10",
    print "If the numbers match, you pass the round"
    #end of giant print block

    #logic for prateek
    command = int(user_input("input number", "random"))
    if command > 10:
        print "Congrats, you thought out of the box"
        print "You now pass to the next round"
        return
    random_number = generateRandomNumber(1, 10)
    if command == random_number:
        print "Congrats, luck is on your side"
        print "You now pass to the next round"
        return
    elif command != random_number:
        print "Whoops, luck is not on your side"
        quit_game()

#Karuns challenge
def karun_challenge():

    print "Do you like sitting on the fence?"
    command  = user_input("y", "n")
    if command == "y":
        print "Do you like going to the gym?"
        command = user_input("y", "n")
        if command == "y":
            print ""
            print "Congrats! You pass to the next round"
            return
        elif command == "n":
            print "You failed the round"
            quit_game()
    elif command == "n":
        print "Whoops! You failed the round"
        quit_game()

#Anshuls Challenge
def anshul_challenge():

    print "Do you like metal?"
    command = user_input("y", "n")
    if command == "y":
        print "Name your favorite metal band"
        command = user_input("Name", "random")
        if command.lower() == "tesseract" or command.lower() == "dream theater":
            print ""
            print "Congrats! You got past the round"
            return
        else:
            print "Can you dab?"
            command = raw_input("y", "n")
            if command == "y":
                print ""
                print "Congrats! You got past The George"
                return
    elif command == "n":
        print "Name your favorite brand of whisky"
        command = user_input("Name")
        if command.lower() == "jack daniels":
            print ""
            print "Congrats! You get past The George"
            return
        else:
            print "Oooh! Sorry, so close! You lose"
            quit_game()

def monil_challenge():
    print "Meet The Gujju"
    print "Do you like saving money?"
    command = user_input("y", "n")
    if command == "y":
        print "What is 150 / 8 % 5"
        command = int(user_input("Monil", "random"))
        if command == 3:
            print ""
            print "Congrats! You passed the round"
            return
    elif command == "n":
        print "Okay, do you like smoking weed?"
        command = user_input("y", "n")
        if command == "y":
            print ""
            print "Congrats! You passed the round"
            return
        elif command == "n":
            print "I'm sorry, we don't have space for squares in this game"
            quit_game()


#function to output choice to user
def user_input(option_1, option_2):
    if option_1 == "y" and option_2 == "n":
        return raw_input("<y/n> ")
    elif option_1 == "input number":
        return raw_input("(1, 10)> ")
    elif option_1 == "Name":
        return raw_input("Name> ")
    elif option_1 == "Monil":
        return raw_input("Answer> ")

def win_game():
    print ""
    print "Congrats you won the game!"
    print "You get absolutely nothing"
    print "Thanks for playing"
    print ""
    exit(0)

start()
