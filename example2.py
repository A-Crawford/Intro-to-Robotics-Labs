user_input = input("Direction to move robot? (Left, Right, Forward, Backward)").lower()

if user_input is not None:
    if user_input == "left":
        print("Moving Left")
    elif user_input == "right":
        print("Moving Right")
    elif user_input == "forward":
        print("Moving Forward")
    elif user_input == "backward":
        print("Moving backward")
    else:
        print("Invalid inpur")
        