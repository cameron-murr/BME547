import pytest

@pytest.mark.parametrize("tuple1, tuple2, x, expected", [
        [tuple(0,0), tuple(2,2), 1, 1]  
        [tuple(-5,2), tuple(10,2), 15, 2]
        [tuple(1,0), tuple(5,-2), 0, 0.5]      
        ])


def test_point_on_line(tuple1, tuple2, x, expected):
    from on_line import point_on_line

    answer = point_on_line(tuple1, tuple2, x)
    assert answer == expected