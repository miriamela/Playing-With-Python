import random

TOTAL_STONES = 20


def main():
    stones_in_game = TOTAL_STONES
    player = 1
    while stones_in_game > 0:
        print("There are "+str(stones_in_game)+" left")
        if player == 1:
            stones = turn_actions(player, stones_in_game)
            player = player + 1
        else:
            stones = turn_actions(player, stones_in_game)
            player = player - 1
        stones_in_game = stones_in_game - stones
        print(" ")
    if stones_in_game < 1:
        if player == 1:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")


def turn_actions(player, stones_in_game):  # entire single turn
    stones = getting_num_stones(player)
    stones = stones_entry_checkers(stones, stones_in_game)
    return stones


def getting_num_stones(player):  # getting stones from player
    stones = int(input("Player "+str(player) +
                 " Would you like to remove 1 or 2 stones? "))
    return stones


def stones_entry_checkers(stones, stones_in_game):  # checker for entries
    while (stones != 2) and (stones != 1):
        stones = int(input("Please enter 1 or 2: "))
    while stones > stones_in_game:
        stones = int(input("There are only "+str(stones_in_game) +
                     " left, please enter "+str(stones_in_game)+" "))
    return stones


if __name__ == "__main__":
    main()
