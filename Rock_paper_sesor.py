while True:
    import random
    user_action = input("Enter a Choice (rock,paper,scissor):")
    possible_action = ["rock","paper","scissor"]
    computer_action = random.choice(possible_action)
    print(f"\n You choice {user_action}. computer choice {computer_action}.\n")
    if user_action == computer_action:
        print("both player selected {user_action}. It's tie")
    elif user_action== "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors You win!")
        else:
            print("paper covers rocks!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper cover rock, YOu win! ")
        else:
            print("scissors cut paper")
    elif user_action == "scissor":
        if computer_action == "rock":
            print("you are loss! rock break scissor")
        else:
            print("scissor cut paper, YOu win!")

    play_again = input("Play again?(y/n):")
    if play_again != "y":
        break

print("This is modification done in the file")