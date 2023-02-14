import random
import keyboard
from tabulate import tabulate
from itertools import cycle
from time import sleep
from player_info import *

tokens = ["Police", "Thief", "Engineer"]
all_info_list = []
scoreboard = []


def play():
    score_A = 0
    score_B = 0
    score_C = 0
    count = 0
    print("It's a 3 players game. Enter your players' name: ")
    players_list = []
    count = 1

    while count <= 3:
        print("Player {}- ".format(count), end=" ")
        players_list.append(str(input()))
        count += 1

    while True:
        store = open("store.txt", "w")
        print(tabulate([[players_list[0]],[players_list[1]],[players_list[2]]], headers=["Player Names"], tablefmt='fancy_grid'))
        print(tabulate([["Police"], ["Thief"], ["Engineer"]], headers=["Tokens"], tablefmt='pretty'))
        print(
            "Random tokens will be assigned to each player. Only police's name will be revealed.\n Police's job is to find the thief between two other players.")
        print('Lets Start. Press ENTER___')

        input()
        cnt = 1
        while cnt <= 5:

            print("__________________")
            if cnt == 5:
                store.write("\nLast shuffle done!\n")
                print("Last shuffle done!")
            else:
                store.write("\nShuffle no.{} done!\n".format(cnt))
                print("Shuffle no.{} done!".format(cnt))

            random.shuffle(tokens)
            player_A = Player(players_list[0], tokens[0], score_A)
            player_B = Player(players_list[1], tokens[1], score_B)
            player_C = Player(players_list[2], tokens[2], score_C)

            all_info_list = [
                player_A,
                player_B,
                player_C
            ]

            for index in all_info_list:
                if index.role == "Thief":
                    thief_name = index.name
                if index.role == "Engineer":
                    index.score += 100

            for index in all_info_list:
                if index.role == "Police":
                    print("{} is the Police.\n{}'s job is to find the thief.Guess who is the thief?".format(index.name,
                                                                                                            index.name))
                    guess = input("Type thief's name: ")
                    if guess == thief_name:
                        index.score += 80
                        print("Congratulations! Right guess!")
                    else:
                        print("Wrong guess! You lose!")
                        for i in all_info_list:
                            if i.role == "Thief":
                                i.score += 50
                                break
            print("Press q+ENTER to see Scoreboard or press any key to proceed")
            val = input()
            while True:
                if val == 'q':  # if key 'q' is pressed
                    print("SCOREBOARD: ")
                    print(tabulate(
                        [["Player Name", "Role", "Total Score"], [player_A.name, player_A.role, player_A.score],
                         [player_B.name, player_B.role, player_B.score],
                         [player_C.name, player_C.role, player_C.score]], headers="firstrow",
                        tablefmt="fancy_grid"))
                    break
                else:
                    break
            store.write(tabulate(
                [["Player Name", "Role", "Total Score"], [player_A.name, player_A.role, player_A.score],
                 [player_B.name, player_B.role, player_B.score], [player_C.name, player_C.role, player_C.score]],
                headers="firstrow", tablefmt="pretty"))
            score_A = player_A.score
            score_B = player_B.score
            score_C = player_C.score
            cnt += 1

            if cnt == 6:
                print("___________________________")
                print("GAME END")
                print("___________________________")
                maximum = max(score_A, score_B, score_C)
                winner_name = []
                for idx in all_info_list:
                    if idx.score == maximum:
                        winner_name.append(idx.name)

        print(tabulate([winner_name], headers=["Winner"], tablefmt="grid",
                       maxcolwidths=[None, 6]))
        store.write("\n")
        store.write(tabulate([winner_name], headers=["Winner"], tablefmt="grid",
                             maxcolwidths=[None, 6]))

        print("\n\t\tThank you for playing the game!!")
        store.close()
        value2 = input("1.Start again.\n2.Exit\n")
        match value2:
            case "1":
                play()
            case "2":
                break


if __name__ == "__main__":
    print("________________________________________________________________")
    print("Welcome to 'WHO'S THE THIEF' game!!!")
    print("________________________________________________________________")
    while True:
        value = input("1.Start the game.\n2.Exit\n")
        match value:
            case "1":
                play()
                break
            case "2":
                break
            case default:
                print("Press again!!")
