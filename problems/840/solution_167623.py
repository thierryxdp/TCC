def bolos(a, b, c):
    x = a//2
    y = b//3
    z = c//5
    if (a, b, c) >= (2, 3, 5):
        return (a + b + c)//10
    if a == 2:
        if (b, c) > (3, 5):
            return 1
        elif c < 5:
            return 0