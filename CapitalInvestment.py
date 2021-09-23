import random

def gameplay(capital, testcases, odds):
    balance = capital
    count = 1
    loses = 0
    wins = 0
    print("\n--- Starting Simulation ---")
    while count <= testcases:
        print(f"Simulation: ({count})")
        print("Starting Balance: ", balance)

        amtplaced = (0.05 * balance)
        print("Amount Placed = ", amtplaced)

        result = random.randint(1, 2)
        if result == 1:
            wins += 1
            balance = balance + (amtplaced * 5)
            print("Round Won")
        elif result == 2:
            loses += 1
            balance = balance - amtplaced
            print("Round Lost")
        print("--"*15)
        count += 1

    print("\nSimulation Ended!")
    print(f"Wins: ({wins}) Loses: ({loses})")
    print(f"Starting Amount: ({capital}), Balance after simulation: ({balance})")




print("\t\t------- The Capital Calculator -------")

capital = input("Provide starting capital: ")
testcases = input("Provide number of test cases: ")

odds = 5

gameplay(int(capital), int(testcases), odds)
