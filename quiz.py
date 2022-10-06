# Define functions
def getFinalScore(questions, points):
    finalScore = round(float(10/questions*points), 1)
    return finalScore

def decideFinalMessage(correct):
    if correct < 11 and correct > 8:
        print("\nJe hebt uitmuntende kennis van achtbanen! Goed gedaan!")
    elif correct < 9 and correct > 6:
        print("\nJe kennis van achtbanen is net zoals ieder ander, gemiddeld :)")
    elif correct < 7 and correct > 4:
        print("\nOei, je weet niet super veel van achtbanen :(")
    elif correct < 5 and correct > 2:
        print("\nMisschien moet je je kennis over achtbanen iets bij laten spijkeren.")
    elif correct < 3 and correct > 0:
        print("\nAY CARAMBA, weet je zo weinig over achtbanen?!")
    else:
        print("\nHelaas, je had alles fout... :(")

# Print the start sequence of the quiz
print("\nWelkom bij de kleine achtbanen quiz!\n")

# Define variable to use in the quiz
antwoord = input("\nWil je beginnen met de quiz?\n")
punten = 0
vragen = 10
antwoorden = [
    "b&m", "bolliger & mabillard", 
    "slc", "suspended looping coaster", 
    "rmc", "rocky mountain construction",
    "b",
    "a",
    "steel vengeance",
    "a",
    "formula rossa",
    "steel dragon 2000",
    "the smiler"
]

# Start the quiz if the user inputs "ja", else don't start the quiz
if antwoord.lower() == "ja":
    print("\nWat leuk! Laten we beginnen!\n\n")

    # Questions one
    antwoord = input("\n1. Welke manufacturer heeft de achtbaan 'fury325' gebouwd?\n")

    # Answers to question one
    if antwoord.lower() == antwoorden[0] or antwoord.lower() == antwoorden[1]:
        punten += 1
        print("\nGOED! Volgende vraag:")
    else:
        print("\nHelaas, het goede antwoord was: B&M. Volgende vraag:")
    
    # Question two
    antwoord = input("2. Om welk achtbaan model staat 'Vekoma' bekend?\n")

    # Answers to question two
    if antwoord.lower() == antwoorden[2] or antwoord.lower() == antwoorden[3]:
        punten += 1
        print("\nGOED! Volgende vraag:")
    else:
        print("\nHelaas, het goede antwoord was: SLC. Volgende vraag:")
    
    # Question three
    antwoord = input("3. Welke manufacturer bouwt houten achtbanen om tot hout en ijzer hybrid achtbanen?\n")

    # Answers to question three
    if antwoord.lower() == antwoorden[4] or antwoord.lower() == antwoorden[5]:
        punten += 1
        print("\nGOED! Volgende vraag:")
    else:
        print("\nHelaas, het goede antwoord was: RMC. Volgende vraag:")

    # Question four
    antwoord = input("4. Wat is de naam van de witte achtbaan in de Efteling?\nA: De Adder\nB: De Python\nC: De Cobra\n")

    if antwoord.lower() == antwoorden[6]:
        punten += 1
        print("\nGOED! Volgende vraag:")
    else:
        print("\nHelaas, het goede antwoord was: B. Volgende vraag:")
    
    # Question five
    antwoord = input("5. Wat is de hoogste achtbaan ter wereld op dit moment?\nA: Kingda Ka\nB: Top-Thrill Dragster\nC: Red Force\n")

    if antwoord.lower() == antwoorden[7]:
        punten += 1
        print("\nGOED! Volgende vraag:")
    else:
        print("\nHelaas, het goede antwoord was: A. Volgende vraag:")
    
    # Question six
    antwoord = input("6. Wat was de aller eerste hyper hybrid achtbaan?\n")

    if antwoord.lower() == antwoorden[8]:
        punten += 1
        print("\nGOED! Volgende vraag:")
    else:
        print("\nHelaas, het goede antwoord was: Steel Vengeance. Volgende vraag:")

    # Question seven
    antwoord = input("7. Welke achtbaan wordt dit jaar aangepast vanwege een ongeluk?\nA: Top-Thrill Dragster\nB: Rip Ride Rock-it\nC: Phantoms revenge\n")

    if antwoord.lower() == antwoorden[9]:
        punten += 1
        print("\nGOED! Volgende vraag:")
    else:
        print("\nHelaas, het goede antwoord was: A. Volgende vraag:")
    
    # Question eight
    antwoord = input("8. Wat is de naam van de achtbaan die het snelheids record verbreekt?\n")

    if antwoord.lower() == antwoorden[10]:
        punten += 1
        print("\nGOED! Volgende vraag:")
    else:
        print("\nHelaas, het goede antwoord is: Formula Rossa. Volgende vraag:")
    
    # Question nine
    antwoord = input("9. Wat is de naam van de langste achtbaan ter wereld?\n")

    if antwoord.lower() == antwoorden[11]:
        punten += 1
        print("\nGOED! Volgende vraag:")
    else:
        print("\nHelaas, het goede antwoord is: Steel Dragon 2000. Volgende vraag:")

    # Question ten
    antwoord = input("10. Wat is de naam van de achtbaan met de meeste loopings?\n")

    if antwoord.lower() == antwoorden[12]:
        punten += 1
        print("\nGOED! Dit was de laatste vraag!")
    else:
        print("\nHelaas... Dit was de laatste vraag!")

    # Calculate final score and print it
    score = getFinalScore(vragen, punten)

    print("\nJou score is: " + str(score))

    # Print a message depending on the final score of the user
    decideFinalMessage(punten)
    
elif antwoord.lower() == "nee":
    print("\nNou dan niet he! >:(\n")
else:
    print("\nDit antwoord ken ik niet...\n")