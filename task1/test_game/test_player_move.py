from task1.game import player_move, game_init, DEFAULT_BOARD

class TestPlayerMove:
    def test_basic(self) -> None:
        s = game_init(2)
        assert player_move(s, 0, 5, DEFAULT_BOARD)
        assert s == [5, 0]
        assert player_move(s, 1, 4, DEFAULT_BOARD)
        assert s == [5, 4]

    def test_over_end(self) -> None:
        s = game_init(1)
        s[0] = 98
        assert player_move(s, 0, 2, DEFAULT_BOARD)
        assert s == [98]

    def test_ladder(self) -> None:
        s = game_init(2)
        assert player_move(s, 0, 2, DEFAULT_BOARD)
        assert s == [38, 0]
        assert player_move(s, 1, 7, DEFAULT_BOARD)
        assert s == [38, 14]

    def test_snake(self) -> None:
        s = game_init(2)
        assert player_move(s, 0, 16, DEFAULT_BOARD)
        assert s == [6, 0]
        assert player_move(s, 1, 62, DEFAULT_BOARD)
        assert s == [6, 19]

    def test_collision(self) -> None:
        s = [5, 6]
        assert player_move(s, 0, 1, DEFAULT_BOARD)
        assert s == [6, 5]

    def test_collision_recursive(self) -> None:
        s = [4, 6, 5]
        assert player_move(s, 0, 2, DEFAULT_BOARD)
        assert s == [6, 5, 4]

    def test_inf_recursion(self) -> None:
        s = [86, 88, 93, 94]
        assert not player_move(s, 0, 1, DEFAULT_BOARD)
