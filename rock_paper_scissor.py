import random

user_wins = 0
computer_wins = 0
options = ["r", "p", "s"]

while True:
    user_input = input("type rock(r)/paper(p)/scissors(s) or quit(q): ").lower()
    if user_input == "q":
        break

    if user_input not in ["r", "p", "s"]:
        continue

    random_number = random.randint(0, 2)
    # r:0, p:1, s:2
    computer_pick = options[random_number]
    print("Computer Pick", computer_pick + ".")

    if user_input == "r" and computer_pick == "s":
        print("you won!")
        user_wins += 1
    elif user_input == "p" and computer_pick == "r":
        print("you won!")
        user_wins += 1
    elif user_input == "s" and computer_pick == "p":
        print("you won!")
        user_wins += 1
    else:
        print("you lost!")
        computer_wins += 1

print("you won",user_wins,'times.')
print("computer won",computer_wins,'times.')
print("goodbye!!")
