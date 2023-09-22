def carros(x,c=5):
    if 0<x<c:
        return 1
    if x>c:
        return (x//c)+1
    elif 0<c<2:
        return x
    else:
        return 0