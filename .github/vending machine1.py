def snack_machine(current_state):

    if current_state == "coin paid":
        return

    if current_state == "locked":
        print("no snack for u")
    elif current_state == "paid":
        print("here u go")
    else:
        print("what do you want from me idk what you're asking")

    current_input = input("You can add a coin (c), ask for a snack (p), or take your snack (t): ")

    if current_state == "locked":
        if current_input == "c":
            current_state = "paid"
        elif current_input == "p":
            print("please insert coin")
        elif current_input == "t":
            print("give me money first")

    elif current_state == "paid":
        if current_input == "c":
            current_state = "unlocked"
            print("coin rejected, take your snack already")
        elif current_input == "p":
            print("take your snack")
            current_state = "unlocked"

    elif current_state == "unlocked":
        if current_input == "t":
            print("here you go")
            current_state = "locked"
        elif current_input == "c":
            print("coin rejected, take your snack already")
        elif current_input == "p":
            print("you already have one you ungrateful child")


    snack_machine(current_state)



snack_machine("locked")