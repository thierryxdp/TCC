def conta_numero(numero,matriz):
    """conta e retorna quantas vezes o numero aparece na matriz
    int,list(list)->int"""
    a=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            b=list.find(numero,matriz)
            if b!=0:
                a+=[b]
    return len(a)