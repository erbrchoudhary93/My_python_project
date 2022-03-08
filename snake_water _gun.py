import random
l=['s','w','g']
chance= 10
no_of_chance=0
computer_point =0
your_point= 0
print("\t \t \t \t  Snake Water Gun Game  \n  \n")
print("s for snake w for water g for gun")

# Making a game in while loop
while no_of_chance<chance:
    input1 =input("Snake , Water ,Gun  : ")
    rendom1= random.choice(l)

    if input1== rendom1:
        print("Tie both 0 point to each \n ")
    elif input1== "s" and rendom1=="g":
        computer_point= computer_point+1
        print(f"your gasses{input1} and computer gasses {rendom1} \n")
        print("Computer wins 1 point \n")
        print(f"Computer point is {computer_point} and your point is {your_point} \n")
    elif input1== "s" and rendom1=="w":
        your_point=your_point+1
        print(f"your gasses{input1} and computer gasses {rendom1} \n")
        print("You wins 1 point \n")
        print(f"Computer point is {computer_point} and your point is {your_point} \n")
    elif input1== "w" and rendom1=="s":
        computer_point= computer_point+1
        print(f"your gasses{input1} and computer gasses {rendom1} \n")
        print("Computer wins 1 point \n")
        print(f"Computer point is {computer_point} and your point is {your_point} \n")
    elif input1== "w" and rendom1=="g":
        your_point=your_point+1
        print(f"your gasses{input1} and computer gasses {rendom1} \n")
        print("You wins 1 point \n")
        print(f"Computer point is {computer_point} and your point is {your_point} \n")
    elif input1== "g" and rendom1=="s":
        your_point=your_point+1
        print(f"your gasses{input1} and computer gasses {rendom1} \n")
        print("You wins 1 point \n")
        print(f"Computer point is {computer_point} and your point is {your_point} \n")
    elif input1== "g" and rendom1=="w":
        computer_point= computer_point+1
        print(f"your gasses{input1} and computer gasses {rendom1} \n")
        print("Computer wins 1 point \n")
        print(f"Computer point is {computer_point} and your point is {your_point} \n")

    else:
        print("You enter wrong input  !!!")
    no_of_chance= no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance}\n")

print("Game Over")
if computer_point>your_point:
    print("Computer wins the game")
elif computer_point==your_point:
    print(" Match Tie")
else:
    print("You wins the Game")

print(f"your point is {your_point} and Computer point is {computer_point}")
