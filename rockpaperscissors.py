import random

    #initally show the score for Player against Computer is 0-0
p_score = 0
c_score = 0
print("Score")
print(p_score)
print(c_score)

    #Lists the total moves possible from a list

moves = ['rock', 'paper', 'scissors']

    #Switch for looping game

game_active = "true"

def player(p_score):
         print(p_score)
         
def computer(c_score):
         print(c_score)
         
def print_scores():
    print("Score")
    player(p_score)
    computer(c_score)

while True:
        #Now we loop the program based on switch
    while game_active == "true":
        
        #Computer move chose randomly from random set of moves
        cmove = random.choice(moves)
        
        #Player move chosen from set of moves listed
        pmove = input("\nWhat is your move: rock, paper, or scissors? ")
        
        #Time to see what computer chose
        print("The computer chose: ",cmove)

        #Now we start to logically define the outcomes:
        #Let's be lazy and grab all possible tie outcomes at once:
        if cmove == pmove:
            print ("Tie")
            print_scores()
    
        if pmove == "rock":
            if cmove == "scissors":
                print("Player Wins!")
                p_score+=1
                print_scores()
                
        if pmove == "rock":
            if cmove == "paper":
                print("Computer Wins!")
                c_score+=1
                print_scores()

        if pmove == "paper":
            if cmove == "rock":
                print("Player Wins!")
                p_score+=1
                print_scores()
                
        if pmove == "paper":
            if cmove == "scissors":
                print("Computer Wins!")
                p_score+=1
                print_scores()
                
        if pmove == "scissors":
            if cmove == "paper":
                print("Player Wins!")
                p_score+=1
                print_scores()
                
        if pmove == "scissors":
            if cmove == "rock":
                print("Computer Wins!")
                c_score+=1
                print_scores()
