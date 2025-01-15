import random
from typing import Generator

# Tuple of (size, snakes, ladders)
Board = tuple[int, dict[int, int], dict[int, int]]
# index - player, value - position
State = list[int]

MAX_ROUNDS = 20
MAX_REC = 100
BOARD_SIZE = 100
# Start tile : End tile
SNAKES = {16: 6, 45: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}
LADDERS = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}
DEFAULT_BOARD: Board = (BOARD_SIZE, SNAKES, LADDERS)

def roll_dice() -> int:
    x = random.randint(1, 6)
    if x == 6:
        print("\t\tHráč hodil 6, háže znovu")
        return x + roll_dice()
    print("\t\tHráč hodil", x)
    return x

def roll_dice_gen() -> Generator[int, None, None]:
    while True:
        yield roll_dice()

def player_move(s: State, active_player: int, roll_val: int, board: Board, rec_cnt: int = 0) -> bool:
    """
    :return: False if recursion limit is reached, True otherwise
    """
    if rec_cnt > MAX_REC:
        print("\t\tPříliš mnoho rekurzí, hra se ukončuje")
        return False

    board_size, snakes, ladders = board

    if s[active_player] + roll_val > board_size - 1:
        print(f"\t\tTah neproběhne, hráč {active_player} by přeskočil cíl")
        return True

    s[active_player] += roll_val
    print(f"\t\tHráč {active_player} se posunul na pole {s[active_player]}")

    if s[active_player] == board_size - 1:
        return True

    if s[active_player] in ladders:
        print(f"\t\tHráč {active_player} se dostal na žebřík, posune se na pole", ladders[s[active_player]])
        s[active_player] = ladders[s[active_player]]
    elif s[active_player] in snakes:
        print(f"\t\tHráč {active_player} šlápl na hada, vrátí se na pole", snakes[s[active_player]])
        s[active_player] = snakes[s[active_player]]

    for player, pos in enumerate(s):
        if player == active_player:
            continue
        if pos == s[active_player]:
            print(f"\t\tHráč {active_player} narazil na hráče {player}, který se vrací o 1 pole")
            if not player_move(s, player, -1, board, rec_cnt + 1):
                return False
    return True

def game_init(players: int) -> State:
    return [0 for _ in range(players)]

def print_state(s: State, game_round: int = -1) -> None:
    if game_round == -1:
        print("Stav na konci hry:")
    else:
        print(f"Stav hry po {game_round}. kole:")
    for player, pos in enumerate(s):
        print(f"\tHráč {player} se nachází na poli {pos}")
    return

def game_loop(s: State, dice: Generator[int, None, None], board: Board) -> int:
    """
    :return: index of the winning player, -1 if the game ends in a draw
    """
    board_size, _, _ = board
    game_round = 0
    while game_round < MAX_ROUNDS:
        print(f"Kolo {game_round}")
        for player in range(len(s)):
            print(f"\tHraje hráč {player}")
            roll_val = next(dice)
            print(f"\t\tHráč {player} dohromady hodil {roll_val}")
            if not player_move(s, player, roll_val, board):
                return -1
            if s[player] == board_size - 1:
                return player
        print_state(s, game_round)
        game_round += 1
    return -1

if __name__ == "__main__":
    players_input = int(input("Zadejte počet hráčů: "))
    if players_input < 1:
        print("Hra musí mít alespoň jednoho hráče")
        exit(1)
    state = game_init(players_input)
    winner = game_loop(state, roll_dice_gen(), DEFAULT_BOARD)
    if winner == -1:
        print("Hra skončila remízou")
    else:
        print(f"Hráč {winner} vyhrál!")
    print_state(state)
