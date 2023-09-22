def carros(x,c=5):
    if 0<x<c:
        return 1
    if c=1:
        return x-c+1
    if x>c:
        return (x//c)+1
    else:
        return 0