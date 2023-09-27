#print welcome message
print("Welcome to Katia's World!")
print("My name is Gucci, and I've puked on my blanket this morning..")
print("Anyways- what is your name traveler?")

#prompt player for calling name
playerName = input("> ")

print("Great! Nice to meet you " + playerName + "!")
print("What type of hero do you want to be? Choose between a Warrior or Mage.")

while True:
    playerClass = input("Enter a valid class: ")
    if(playerClass == "Warrior".lower()):
        playerWeapon = "sword"
        print("You have chosen Warrior! Great choice - strength will be your ally.")
        break
    elif(playerClass.lower() == "Mage".lower()):
        playerWeapon = "wand"
        print("You have chosen Mage! Intelligence will be your companion.")
        break
    else:
        print("Invalid choice. Please enter Warrior or Mage.")

print("Let's begin your journey! You travel into a forest and you encoutner a dragon. Do you fight? Yes or no?")
fightChoice = input("> ")

if(fightChoice == "Yes".lower()):
    print("Great! Grab your " + playerWeapon + " and lets rock and roll!")

elif(fightChoice == "No".lower()):
    print("Too bad! For the purposes of this mini game, you will fight! Grab your " + playerWeapon + " and let's fight!")

else:
    print("I'll just make you fight! Grab your " + playerWeapon + " and let's fight!")
