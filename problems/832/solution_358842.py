def eh_quadrada(x):
    a=len(x)
    b=len(x[0])
    if a == b:
        return True
    elif x == [[]]:
        return True
    else:
        return False