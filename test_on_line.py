import pytest


@pytest.mark.parametrize("tuple1, tuple2, x, expected", [
        [(0, 0), (2, 2), 1, 1],
        [(-5, 2), (10, 2), 15, 2],
        [(1, 0), (5, -2), 0, 0.5],
        ])
def test_point_on_line(tuple1, tuple2, x, expected):
    from on_line import point_on_line

    answer = point_on_line(tuple1, tuple2, x)
    assert answer == expected


@pytest.mark.parametrize("tuple1, tuple2, tuple3, expected", [
        [(0, 0), (2, 2), (1, 1), True],
        [(-5, 2), (10, 2), (15, 0), False],
        [(1, 0), (5, -2), (0, 0.5), True],
        ])
def test_in_point_in_line(tuple1, tuple2, tuple3, expected):
    from on_line import is_point_in_line

    answer = is_point_in_line(tuple1, tuple2, tuple3)
    assert answer == expected
