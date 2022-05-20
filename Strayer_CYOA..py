#------------------------------------
from asyncore import write
import sys,time,os,random
from tkinter.messagebox import YES

def typewriter(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.00)
        else:
            time.sleep(0.00)
            
#------------------------------------

def writeInput(noneHelp):
    typewriter(noneHelp)
    var = input()
    typewriter("\n")
    return var

def d20Roll():
    return random.randint(1, 20)




computerLaunch = writeInput("Would you like to power me on?\nPlease type YES or NO and press ENTER to continue.     \n")
if computerLaunch.lower() == "yes":
    string = "...\n..\n.\n"
    typewriter(string)
    string = "Hello and welcome to my Choose Your Own Adventure!.\nWhen prompted to answer a question, please type your response following the query and then press ENTER to continue.\n"
    typewriter(string)
    string = "...\n..\n.\n"
    typewriter(string)
    typewriter("Starting now, you will be prompted to roll a dice, and using the numbers from the dice,\nyou will assign a random set of skill points to a given skill, based on what you roll.\nThese skills will dictate parts of your story in the future and may open, or close certain pathways for you in the future.\n")
    typewriter("...\n..\n.\n")
    typewriter("Before we roll for our stats, I am going to explain them to you.\n")
    typewriter("\n\n")
    typewriter("Strength, or (STR is the measurement of ones physical power.\n")
    typewriter("Dexterity, or (DEX) is a measurement of ones agility and speed.\n")
    typewriter("Constitution, or (CON) is the threshold of how much someone can withstand.\n")
    typewriter("Intelligence, or (INT) is how smart you are.\n")
    typewriter("Wisdom, or (WIS) is the measurement of ones common sense and intuition.\n")
    typewriter("Charisma, or (CHA) is the measurement of how you can charm and influence others.\n")
    typewriter("\n\n")
    typewriter("Now that we have gone over our basic stats and what they mean, you are now going to roll for your stat points.\nThe higher the roll, the better.\n")
    typewriter("...\n\n")
    rollStr = writeInput("type ROLL STR to continue.     \n")
    if rollStr.lower() == "roll str":
        strValue = d20Roll()
        if strValue <21:
            typewriter(f"You rolled a {strValue} for your strength skill\n")

            rollDex = writeInput("type ROLL DEX to continue.     \n")
            if rollDex.lower() == "roll dex":
                dexValue = d20Roll()
                if dexValue <21:
                    typewriter(f"You rolled a {dexValue} for your dexterity skill.\n")

                    rollCon = writeInput("type ROLL CON to continue.     \n")
                    if rollCon.lower() == "roll con":
                        conValue = d20Roll()
                        if conValue <21:
                            typewriter(f"You rolled a {conValue} for your constitution skill.\n")

                            rollInt = writeInput("type ROLL INT to continue.     \n")
                            if rollInt.lower() == "roll int":
                                intValue = d20Roll()
                                if intValue <21:
                                    typewriter(f"You rolled a {intValue} for your intelligence skill.\n")

                                    rollWis = writeInput("type ROLL WIS to continue.     \n")
                                    if rollWis.lower() == "roll wis":
                                        wisValue = d20Roll()
                                        if wisValue <21:
                                            typewriter(f"You rolled a {wisValue} for your wisdom skill.\n")

                                            rollCha = writeInput("type ROLL CHA to continue.     \n")
                                            if rollCha.lower() == "roll cha":
                                                chaValue = d20Roll()
                                                if chaValue <21:
                                                    typewriter(f"You rolled a {chaValue} for your charisma skill.\n")
                                                    
                                                    statCont = writeInput("Your stats are\nSTR = " + strValue + "\nDEX = " + dexValue + "\nCON = " + conValue + "\nINT = " + intValue + "\nWIS = " + wisValue + "\n\nPlease type CONTINUE to continue onto the game!     \n")
                                                    if statCont.lower() == "continue":
                                                        typewriter(string)
                                                        speechDie = writeInput("Please List one Verb:    \n")
                                                        speechBeds = writeInput("What is the last place you would want to die?   \n")
                                                        speechDays = writeInput("What is something you could fight for?   \n")
                                                        speechLives = writeInput("What is your guilty pleasure food?   \n")
                                                        speechFreedom = writeInput("What is your guilty pleasure restaurant?   \n")
                                                        speechWeapon = writeInput("What is your weapon of choice to take into battle?   \n")
                                                        typewriter(string)
                                                        string = "\nYou awake one morning to find yourself wrapped in bandages...\n\
                                                        You then look around and notice an elderly lady dipping a washcloth in hot soapy water...\n\
                                                        The elderly lady looks over at you, noticing you're awake and asks you\n"
                                                        string = "\n"
                                                        typewriter(string)
                                                        userName = writeInput("What is your name?     \n")
                                                        typewriter("Why hello there, " + userName + ", I am Ingrid. I have been watching over you while you recover\n")
                                                        conditionStatus = writeInput("And how are you feeling, now that you are awake?     \n")
                                                        typewriter("\nYou sit up after answering the elderly womans qestions, trying to remember what happened and who you are to no avail...\n")
                                                        typewriter("you fall back into your bed, closing your eyes as you drift back into unconsciousness...\n")
                                                        knowledgeAnswer = writeInput("\nIngrid wakes you and asks: 'would you like to know what happened to you?'     \n")
                                                        if knowledgeAnswer.lower() == "yes":
                                                            typewriter("You nod politely in reply to her\n")
                                                            typewriter(string)
                                                            typewriter("\nThe most I can recall is you went down with a fight, your " + speechWeapon + " bloodied by your slain foes...")
                                                            typewriter("from what I hear, you were glorious, beginning the fight with the most powerful speech I had ever heard")
                                                            typewriter("you proclaimed your name to be " + userName + " and then went on to say")
                                                            typewriter("\nAye, fight and you may " + speechDie + ". Run and you’ll live, at least a while.")
                                                            typewriter("And dying in your " + speechBeds + " many years from now,")
                                                            typewriter("would you be willing to trade all the " + speechDays + " from this " + speechDays + " to that for one chance,")
                                                            typewriter("just one chance to come back here and tell our enemies that they may take our " + speechLives + ",")
                                                            typewriter("\nIngird: Before ending your speech you rallied everyone to gether by ending it with")
                                                            typewriter("\nbut they’ll never take our " + speechFreedom + "!")
                                                            typewriter(string)
                                                        else:
                                                            typewriter("Well, thats too bad then isnt it?\n")
                                                            typewriter("The elderly woman sighs at you, rolling her eyes\nWell at the very least drink some tea\n")
                                                            typewriter("The elderl woman hands you a hot cup of tea\nyou take the tea gracefully into your hands as you begin to sip on it\nyour consciousness begins to fade as you drink\n")
                                                            typewriter("You yell at the elderly woman 'what the hell was in th-'\nBefore being able to finish your sentence you fall back into your bed, passing out\n")
                                                            typewriter("...\n..\n.\n")
                                                            typewriter("You awake to see a group of armed guards sitting next to you, they poke you with the wooden shaft of their pikes\nWhat do you think you're doing here? Drunken and nude, passed out in this womans home!\n")
                                                            typewriter("Get up! You're coming with us!\n")
                                                            fightStay = writeInput("Do you choose to FIGHT the guards or SURRENDER to them?     \n")
                                                            if fightStay.lower() == "fight":
                                                                typewriter("You get up and lunge at the guards, attempting to tackle one as you are successful in doing so,\nlanding onto the ground ontop of the guardsmen you feel a sharp, ripping pain in your back and your chest\n")
                                                                typewriter("Oi, you really think that was a good idea boy?\n")
                                                                typewriter("You look down, seeing you've been impaled on one of the guards pikes.\n")
                                                                finalWords = writeInput("What are your final words boy?     \n")
                                                                typewriter("You fall back, uttering " + finalWords + " as you die.\n...\n..\n.\n")
                                                                typewriter("G A M E - O V E R\n...\n..\n.")
                                                                sys.exit() 

                                                            elif fightStay.lower() == ("surrender"):
                                                                string = "The guards motion for you to get onto your knees and put your hands up into the air.\n"
                                                                typewriter("You do as you are told and get onto your knees, raising your nabbers high into the air.\n")
                                                                typewriter("You sit there, wondering how you ended up getting yourself into this mess as you are cuffed and pulled away from the womans home.\n...\n..\n.\n")
                                                                typewriter("You arrive at the guard house and are promptly thrown into a dank and crusty cell.\n You sit there and contemplate your life decisions as you look around for options.\n")
                                                                lookingAssess = writeInput("\nWhich way do you decide to look around?\nLeft or Right?     \n")
                                                                if lookingAssess.lower() == "left":
                                                                    typewriter("You look over and to your left, examining every inch of that part of the cell...\nYou notice a nail file layong on the ground, as you take note of its presence.\n")
                                                                    typewriter("You sit back, having assessed your situation\n")
                                                                    prisonBreak1 = writeInput("What do you decide to do? Grab the nail file and ESCAPE or WAIT for your guardsman to come through.\n")

                                                                elif lookingAssess.lower() == ("right"):   
                                                                    string = "You take a short gander over to the Right side of the cell and find nothing but rubble and some broken bones with deep gnaw marks\n"
                                                                    typewriter("You sit back into your concrete bed, pondering what you should do next after having assessed your situation and your options.\n")
                                                                    typewriter(string)
                                                                    prisonBreak2 = writeInput("What do you decide to do? Grab the nail file and ESCAPE or WAIT for your guardsman to come through.\n")
                                                                    if prisonBreak2.lower() == "ESCAPE":
                                                                        typewriter("Youo go over to the other side of the cell and grab some rocks.\nYou think you could smash these together with the bone and make a lockpick!\nYou do exactly that, toiling away while trying to not be seen by the patrolling guards\n")
                                                                        typewriter("You will need to roll for DEXTERITY to continue...\n")
                                                                        roll = writeInput("type ROLL to continue     \n")
                                                                        if roll.lower() == "roll":
                                                                            separateChoice = ['1 - path 1 succeeds\n', '2 - path 2 fails\n', '3 - path 3 succeeds\n', '4 - path 4 fails\n']
                                                                            value = random.choice(separateChoice)
                                                                            typewriter(value)
                                                                            if value == "1 - path 1 succeeds\n":
                                                                                typewriter("congrats on winning. I wll now power off.\n...\n..\n.")
                                                                            elif value == "2 - path 2 fails\n":
                                                                                typewriter("Congrats you have failed successfully!\nI will now power off\n...\n..\n.")
                                                                            elif value == "'3 - path 3 succeeds\n":
                                                                                typewriter("Congrats you have succeeded\n")
                                                                            elif value == "4 - path 4 fails\n":
                                                                                typewriter("You have failed\n")



elif computerLaunch.lower() == ("no"):
    string = "Powering off in.\n3...\n2..\n1.\n"
    typewriter(string)
    import sys

    sys.exit()

