from problem_solution import intercala


def test_intercala():
    assert intercala([1, 3, 5], [2, 4, 6]) == [1, 3, 5, 2, 4, 6, 1, 3, 5]
