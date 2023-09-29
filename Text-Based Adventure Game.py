import random

def fightMode(playerHP, enemyHP, enemy):
  fightMode = True
  while fightMode:
    print(playerAbilities)

    #select an attack
    while True:
      attackChoice = int(
          input("Enter a number between 1-4 to select an attack: "))
      if (1 <= attackChoice < 5):
        attackDamage = playerAbilities[attackChoice][1]
        break
      else:
        print("Invalid choice, try again.")

    #attack hitting
    print("You used " + playerAbilities[attackChoice][0] + " which did " + \
          str(attackDamage))
    enemyHP = max(0, enemyHP - attackDamage)
    print(enemy + " has " + str(enemyHP) + "/100 HP left.")

    #enemy's attack
    if(enemyHP > 0):
      enemyAttack = random.randint(5, 20)
      print("The " + enemy + " attacked and did " + str(enemyAttack) +
            " damage!")
      playerHP = max(0, playerHP - enemyAttack)
      print("You have " + str(playerHP) + "/100 HP left.")
  
    #check for HP
    if (playerHP > 0 and enemyHP > 0):
      continue
    elif (enemyHP <= 0):
      print("You defeated the " + enemy + "!")
      fightMode = False
    else:
      print("You died.")
    fightMode = False
def addXP(gainXP):
  global playerXP 
  playerXP += gainXP
  return playerXP

playerXP = 0

#print welcome message
print("Welcome to Adventure Land!")
print("My name is Butler, and I've puked on my blanket this morning..")
print("Anyways- what is your name traveler?")

#prompt player for calling name
playerName = input("> ")

print("Great! Nice to meet you " + playerName + "!")

#prompt player to choose a class
print("What type of hero do you want to be? Choose between a Warrior or Mage.")
while True:
  playerClass = input("Enter a valid class: ")
  if (playerClass == "Warrior".lower()):
    playerWeapon = "sword"
    playerAbilities = {
        1: ["Tackle", random.randint(10, 20)],
        2: ["Slash", random.randint(5, 40)],
        3: ["Stab", 30],
        4: ["Cannon", random.randint(0, 80)]
    }
    print(
        "You have chosen Warrior! Great choice - strength will be your ally.")
    break
  elif (playerClass.lower() == "Mage".lower()):
    playerWeapon = "wand"
    playerAbilities = {
        1: ["Fireball", random.randint(15, 25)],
        2: ["Electric Chair", random.randint(10, 50)],
        3: ["Empowering hit", 40],
        4: ["Rock push", random.randint(30, 60)]
    }
    print("You have chosen Mage! Intelligence will be your companion.")
    break
  else:
    print("Invalid choice. Please enter Warrior or Mage.")

#prompt for fight choice
print("Let's begin your journey! You travel into a forest and you encoutner a dragon." \
      " Do you fight? Yes or no?")
fightChoice = input("> ")

if(fightChoice == "Yes".lower()):
    print("Great! Grab your " + playerWeapon + " and lets rock and roll!")
elif(fightChoice == "No".lower()):
    print("Too bad! For the purposes of this mini game, you will fight! Grab your " \
          + playerWeapon + " and let's fight!")
else:
    print("I'll just make you fight! Grab your " + playerWeapon + " and let's fight!")

#commence dragon fight
print("Let's begin the fight!")
fightMode(100, 100, "dragon")
addXP(15)
print("You have " + str(playerXP) + " XP!")
