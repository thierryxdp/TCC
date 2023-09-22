def bolos (a, b, c):
    #para cada bolo é necessario 2a, 3b, 5c
    if a > 0 and b > 0 and c > 0 and (a+b+c)%10 == 0:
        return(a+b+c)/10
    '''if (a+b+c)%10 == 0:
        return (a+b+c)/10'''
    elif a < 2 or b < 3 or c < 5:
        return 0