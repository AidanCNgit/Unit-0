import random

pscoe = 0
cs = 0

def main():

    #i took the easy way out :( VVV
    global pscoe
    global cs
    #^^^^^^^^^^^^^

    playing = True
    tied = True

    ch1 = random.randint(1, 3)
    ch2 = random.randint(1, 3)

    ch1 = n2h[ch1]
    ch2 = n2h[ch2]

    uh1 = int(input("rock(1), scissors(2), or paper(3)?"))
    uh2 = int(input("Sorry, one more time : rock(1), scissors(2), or paper(3)?"))

    uh1 = n2h[uh1]
    uh2 = n2h[uh2]

    print(f"You chose {uh1} and {uh2}")
    print(f"Your opponent has chosen {ch1} and {ch2}")

    ufh = int(input("Which hand do you want to keep? (1, 2)"))
    cfh = random.randint(1, 2)

    ufh = uh1 if ufh == 1 else uh2
    cfh = ch1 if cfh == 1 else ch2

    print(f"You have chosen {ufh}, and your opponent has chosen {cfh}")

    match ufh:

        case "rock":

            tied = False if cfh == "scissors" or cfh == "paper" else True
            print("You Lose :(") if cfh == "paper" else print("You Win! :)") if cfh == "scissors" else print("Tie! Go Again!")
            cs += 1 if cfh == "paper" else 0
            pscoe += 1 if cfh == "scissors" else 0

        case "paper":

            tied = False if cfh == "rock" or cfh == "scissors" else True
            print("You Lose :(") if cfh == "scissors" else print("You Win! :)") if cfh == "rock" else print("Tie! Go Again!")
            cs += 1 if cfh == "scissors" else 0
            pscoe += 1 if cfh == "rock" else 0

        case "scissors":

            tied = False if cfh == "rock" or cfh == "paper" else True
            print("You Lose :(") if cfh == "rock" else print("You Win! :)") if cfh == "paper" else print("Tie! Go Again!")
            cs += 1 if cfh == "rock" else 0
            pscoe += 1 if cfh == "paper" else 0

    playing = False if input("Enter q to Quit") == "q" else True

    main() if tied or playing else print(f"Thanks for playing, your score was {pscoe}, while your opponents was {cs}")

n2h = {

    1 : "rock",

    2 : "scissors",

    3 : "paper",

}

main()