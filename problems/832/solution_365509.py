def eh_quadrada(matriz):
    n1=0
    n2=0
    i=0
    j=0
    for i in enumerate(matriz):
        n1 += 1
        for j in enumerate(i):
            n2 += 1
    if n1 == n2 or n1 == 0: 
        return True
    else:
        return False