def bolos(a, b, c):
    if a / 2 >= 1 and b / 3 >= 1 and c / 5 >= 1:
        return min(a // 2, b // 3, c // 5)
    return 0