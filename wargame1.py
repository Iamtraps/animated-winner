import random
done=False
aiName=["United States", "India", "China", "Iran", "United Kingdom", "switzerland", "ecuador"]
aiNameTwo=["1","2","3"]
aiChoice = random.randrange(0,7)
if aiChoice == 0:
    aiChoice = aiName[0]
if aiChoice == 1:
    aiChoice = aiName[1]
if aiChoice == 2:
    aiChoice = aiName[2]
if aiChoice == 3:
    aiChoice = aiName[3]
if aiChoice == 4:
    aiChoice = aiName[4]
if aiChoice == 5:
    aiChoice = aiName[5]
if aiChoice == 4:
    aiChoice = aiName[6]
playerHealth=100   
playerTroops = int(100)

def cls(): print("\n" * 40)
print("""
                _____________________________________________________
                |                                                   |
                |     ____    _____    ____  _____  _______         |
                |     \   \   |   |   /   / /     \ \  ___ \        |
                |      \   \  |   |  /   / /  /_\  \ \ \  \_\       |
                |       \   \_|   |_/   / /  /   \  \ \ \           |
                |        \_____________/ /__/     \__\ \_\          |
                |___________________________________________________|
""")
input()
cls()
while not done:
    #values
    randChoiceTroops = playerTroops + 50 + random.randrange(0,100)
    aiTroops = 200
    aiHealth=400
    playerLand=50
    aiLand=50
    #
    playerName=input("Please come up with a name for your country: ")
    print()
    print( playerName + ", This sounds like a great country")
    print()
    input("press ENTER to continue")
    cls()
    print("Your opponent is: " + aiChoice)
    print("They have started out with " + str(aiHealth) +" Health : " + str(aiTroops) + " Troops")
    input()
    print("You, " + str(playerName) + " have started out with " + str(playerHealth) + " Health : " + str(playerTroops) + " Troops")
    input()
    cls()
    print("Your options will be listed below: ")
    input()
    while playerHealth != 0 or aiHealth != 0 or playerLand != 0 or aiLand != 0:
        if playerHealth <= 0 or playerLand <= 0:
            input("Sorry you have lost the game")
            break
        if aiHealth <= 0 or aiLand <= 0:
            print("Congratulations" + playerName + "you have won the game!")
            input()
            break
        aiChoiceTwo = random.randrange(0,4)
        if aiChoiceTwo == 0:
            aiTroops = aiTroops + randChoiceTroops
        if aiChoiceTwo == 1:
            aiHealth = aiHealth + 50
        if aiChoiceTwo == 2:
            if playerTroops > aiTroops:
                aiHealth = aiHealth - random.randrange(50, 100)
                playerHealth = playerHealth - random.randrange(0,50)
                playerTroops = playerTroops - playerTroops % aiTroops
                aiTroops = aiTroops - playerTroops % aiTroops
            if aiTroops > playerTroops:
                playerHealth = playerHealth - random.randrange(50, 100)
                aiHealth = aiHealth - random.randrange(0,50)
                aiTroops = aiTroops - aiTroops % playerTroops
                playerTroops = playerTroops - aiTroops % playerTroops
            if playerHealth <= 0 or playerLand <= 0:
                input("Sorry you have lost the game")
                break
            if aiHealth <= 0 or aiLand <= 0:
                print("Congratulations, " + playerName + " you have won the game!")
                break
        cls()
        print()
        print("Your remaining troops are: " + str(playerTroops))
        print("your health is now: " + str(playerHealth))
        print()
        print(aiChoice + ", has this many troops: " + str(aiTroops))
        print(aiChoice + ", has this much health: " + str(aiHealth) )
        print()
        print("1. Build Troops")
        print("2. Upgrade Health")
        print("3. Fight")
        print("4. Flee")
        print("5. Clear Screen")
        if playerHealth == 1:
           print("nuke available... Type NUKE")
           nuke= -1000000000
        selection = input("Which do you choose to do?: ")
        if playerHealth == 1 and selection == "NUKE":
            aiHealth = aiHealth + nuke
            if aiTroops > playerTroops:
                playerHealth = playerHealth - random.randrange(50, 100)
                aiHealth = aiHealth - random.randrange(0,50)
                iTroops = aiTroops - aiTroops % playerTroops
                playerTroops = playerTroops - aiTroops % playerTroops
                input()
        if selection == "1":
            playerTroops = playerTroops  + randChoiceTroops
        if selection == "2":
            playerHealth = playerHealth + 50
            input("Upgrading health...")
        if selection == "3":
            if playerTroops > aiTroops:
                aiHealth = aiHealth - random.randrange(50, 100)
                playerHealth = playerHealth - random.randrange(0,50)
                playerTroops = playerTroops - playerTroops % aiTroops
                aiTroops = aiTroops - playerTroops % aiTroops
            if aiTroops > playerTroops:
                playerHealth = playerHealth - random.randrange(50, 100)
                aiHealth = aiHealth - random.randrange(0,50)
                iTroops = aiTroops - aiTroops % playerTroops
                playerTroops = playerTroops - aiTroops % playerTroops
                input()
            if playerHealth <= 0 or playerLand <= 0:
                input("Sorry you have lost the game")
                break
            if aiHealth <= 0 or aiLand <= 0:
                print("Congratulations" + playerName + "you have won the game!")
                break
        if selection == "4":
            input("That is unfortunate")
            break
        if selection == "5":
            cls()
        if selection =="":
            input()
        
