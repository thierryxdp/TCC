def eh_quadrada(matriz):
    i=0
    j=0
    n1=0
    n2=0
    for i in enumerate(matriz):
        n1+=1
        for j in enumerate(i):
            n2+=1
    return n2