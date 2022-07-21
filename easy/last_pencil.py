"""
Last Pencil Project (from JetBrains Academy):
The objective was to build a game while practicing some Python basics.
It's a fun project to practice fundamentals.
Easy ~ 9 hours to complete

For more details, check out:
https://hyperskill.org/projects/258
"""
import random


def is_numeric_value(usr_input: str) -> bool:
    is_numeric: bool = False

    if usr_input.isdigit():
        is_numeric = True

    return is_numeric


def ask_num_pencils() -> int:
    msg_error_numeric: str = "The number of pencils should be numeric"
    msg_error_positive: str = "The number of pencils should be positive"

    usr_input = input()

    if not is_numeric_value(usr_input):
        print(msg_error_numeric)
        return -1

    num_pencils: int = int(usr_input)

    if num_pencils == 0:
        print(msg_error_positive)
        return -1

    return int(num_pencils)


def ask_first_player() -> str:
    PLAYERS: set[str] = {'John', 'Jack'}
    msg_choose: str = "Choose between John and Jack"

    first_player = input()

    if first_player not in PLAYERS:
        print(msg_choose)
        return ""

    return first_player


def remove_pencils(num_pencils: int) -> int:
    POSSIBLE_VALUES: set[int] = {1, 2, 3}
    msg_error_wrong_val: str = "Possible values: '1', '2' or '3'"
    msg_error_too_many: str = "Too many pencils were taken"

    usr_input = input()

    if not is_numeric_value(usr_input):
        print(msg_error_wrong_val)
        return -1

    num_removed_pencils: int = int(usr_input)

    if num_removed_pencils not in POSSIBLE_VALUES:
        print(msg_error_wrong_val)
        return -1

    if num_removed_pencils > num_pencils:
        print(msg_error_too_many)
        return -1

    return num_removed_pencils


def set_players(current_player: str) -> str:
    next_player: str = ""

    if current_player == "John":
        next_player = "Jack"
    elif current_player == "Jack":
        next_player = "John"

    return next_player


def generate_losing_sequence(nth_term: int) -> list[int]:
    STEP = 4
    sequence: list[int] = [1]
    while sequence[-1]+STEP <= nth_term:
        sequence.append(sequence[-1] + STEP)

    return sequence


def is_winning_position(num_pencils, losing_sequence) -> bool:
    is_win_pos: bool = False
    if num_pencils not in losing_sequence:
        is_win_pos = True

    return is_win_pos


def remove_pencils_bot(num_pencils) -> int:
    num_removed_pencils: int = 1

    if num_pencils != 1:
        losing_sequence: list[int] = generate_losing_sequence(num_pencils)

        if is_winning_position(num_pencils, losing_sequence):
            num_removed_pencils = num_pencils - losing_sequence[-1]
        else:
            number_list = [1, 2, 3]
            if num_pencils >= 3:
                num_removed_pencils = random.choice(number_list)
            elif num_pencils == 2:
                num_removed_pencils = random.choice(number_list[:2])

    return num_removed_pencils


def main() -> None:
    USR_BOT = "Jack"
    msg_pencils: str = "How many pencils would you like to use:"
    msg_who_first: str = "Who will be the first (John, Jack):"
    num_pencils: int = -1
    num_removed_pencils: int = -1
    current_player: str = ""
    next_player: str = ""
    pencils_str: str = ""

    # First, we're going to set the number of pencils for the game
    print(msg_pencils)
    while num_pencils == -1:
        num_pencils = ask_num_pencils()

    # Next, we set the first player
    print(msg_who_first)
    while current_player == "":
        current_player = ask_first_player()

    # After that set the second player accordingly
    next_player = set_players(current_player)

    # Finally, set the pencils to play with
    for _ in range(num_pencils):
        pencils_str += '|'

    print(pencils_str)

    # Game logic
    while num_pencils > 0:
        print(f"{current_player}'s turn:")

        if current_player == USR_BOT:
            num_removed_pencils = remove_pencils_bot(num_pencils)
            print(num_removed_pencils)
        else:
            while num_removed_pencils == -1:
                num_removed_pencils = remove_pencils(num_pencils)

        num_pencils = num_pencils - num_removed_pencils

        if num_pencils > 0:
            print(pencils_str[:num_pencils])

        # Set next round
        current_player, next_player = next_player, current_player
        num_removed_pencils = -1

    print(f"{current_player} won!")


if __name__ == '__main__':
    main()
