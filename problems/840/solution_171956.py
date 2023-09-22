def bolos (a, b, c):
    #para cada bolo é necessario 2a, 3b, 5c
    if (a+b+c)%10 == 0:
        return (a+b+c)/10
    elif a < 2 or and b < 3 or and c < 5:
        return 0