from problem_solution import intercala


def test_intercala():
    assert intercala([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_intercala_2():
    assert intercala([7, 9, 11], [8, 10, 12]) == [7, 8, 9, 10, 11, 12]
