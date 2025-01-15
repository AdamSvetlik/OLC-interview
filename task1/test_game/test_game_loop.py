from typing import Generator
from task1.game import game_init, game_loop, DEFAULT_BOARD

def const_gen(n: int) -> Generator[int, None, None]:
    while True:
        yield n

class TestGameLoop:
    def test_win(self) -> None:
        board = (5, {}, {})
        s = game_init(1)
        assert game_loop(s, const_gen(1), board) == 0

    def test_over_end(self) -> None:
        board = (5, {}, {})
        s = game_init(1)
        assert game_loop(s, const_gen(3), board) == -1

    def test_inf_snake(self) -> None:
        board = (5, {2: 1}, {})
        s = game_init(1)
        assert game_loop(s, const_gen(1), board) == -1

    def test_inf_recursion(self) -> None:
        s = [86, 88, 93, 94]
        assert game_loop(s, const_gen(1), DEFAULT_BOARD) == -1

    def test_inf_collision(self) -> None:
        board = (5, {}, {})
        s = game_init(2)
        assert game_loop(s, const_gen(1), board) == -1

    def test_collision_to_ladder_end(self) -> None:
        board = (5, {}, {1:4})
        s = [2, 0]
        assert game_loop(s, const_gen(1), board) == 1