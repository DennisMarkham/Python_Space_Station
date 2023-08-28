
talos = {
    "lift": "unlocked",
    "arboretum airlock": "unlocked",
    "arboretum/crew quarters": "unlocked",
    "arboretum/deep stoarge": "unlocked",
    "deep storage airlock": "unlocked",
    "arboretum/guts": "unlocked",
    "lobby/guts": "unlocked",
    "lobby/hardware labs": "unlocked",
    "hardware labs airlock": "unlocked"
    }

def lockdown():
    for x in talos:
        talos[x] = "locked"
    display()


def delockdown():
    for x in talos:
        talos[x] = "unlocked"
    display()
    
    


def display():
    pretty_display()
    menu()

def pretty_display():
    print("*** \n")
    for x in talos:
        print(x + ": " + talos[x] + "\n")
    print("***\n")
def select():
    select_choice = input("1) Toggle door\n2) Display doors\n3) Return to main menu\n")
    if select_choice == "1":
        toggle()
    elif select_choice == "2":
        print(talos)
        select()
    elif select_choice == "3":
        menu()
    else:
        print("I did not catch that")
        select()

def toggle():
    door_choice = input("Enter door name, or type 'back' to return to main menu:\n")
    if talos[door_choice] == "locked":
        talos[door_choice] = "unlocked"
        display()
    elif talos[door_choice] == "unlocked":
        talos[door_choice] = "locked"
        display()
    else:
        if door_choice == "back":
            menu()
        else:
            print("I'm sorry, there is no such door")
            toggle()
        
def menu():
    menu_choice = input("Welcome to the Talos 1 control center.  Please enter one of the following" +
      " commands:\n" + "1)Initiate Lockdown\n2)Full access\n3)Display\n4)Toggle individual doors \n")
    if menu_choice == "1":
        lockdown()
    elif menu_choice == "2":
        delockdown()
    elif menu_choice == "3":
        display()
    elif menu_choice == "4":
        select()
    else:
        print("Please enter a number")

menu()


