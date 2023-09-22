def repetidos(lista):
    n=len(lista)
    prox=n-1
    num=0
    while prox>0:
        if lista[prox]==lista[prox-1]:
            num=num+1
        prox=prox-1
    return num