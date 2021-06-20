import random
import easygui
list1 = ["Yes", "No"]
for i in range(5, 0, -1):
    a = random.randint(1, i)
    if a == 1:
        if i % 2 == 0:
            easygui.msgbox("Your opponent died", "Prompt")
            break
        else:
            easygui.msgbox("You died", "Prompt")
            break
    else:
        if i % 2 == 0:
            easygui.msgbox("Your opponent survived", "Prompt")
        else:
            easygui.msgbox("You survived", "Prompt")
    if i != 0:
        x = easygui.buttonbox("Do you want to continue?" + " " + str(i), "Prompt", list1)
        if x == "Yes":
            continue
        else:
            break