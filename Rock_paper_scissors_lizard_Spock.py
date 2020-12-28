import random
def name_to_number(name):
    if name == "Rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "Paper":
        return 2
    elif name == "Lizard":
        return 3
    elif name == "Scissors":
        return 4
    else:
        print ("Error : Wrong Input")
    return name

def number_to_name(number):
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "Paper"
    elif number == 3:
        return "Lizard"
    elif number == 4:
        return "Scissors"
    else:
        print ("Error: Wrong Input")
    return name

def rpsls(player_choice):
    #step 3 working
    print ("")
    print("Player Choice: ",player_choice)
    player_number = name_to_number(player_choice)
    #step 4
    #random number generator, otherwise str error in step 5
    rr = (random.randrange(0,5)) 
    comp_number = number_to_name(rr)
    print ("Computer Choice: ", comp_number)
    #step 5
    if (rr + 1) % 5 == player_number:
        print ("Player wins !")
    elif (rr + 2) % 5 == player_number:
        print ("Player wins !")
    elif rr == player_number:
        print ("Player and computer tie !")
    else:
        print ("Computer wins !")
        
rpsls("Rock")
rpsls("Spock")
rpsls("Paper")
rpsls("Lizard")
rpsls("Scissors")
