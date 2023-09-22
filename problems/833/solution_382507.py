def conta_numero(numero,matriz):
    """conta e retorna quantas vezes o numero aparece na matriz
    int,list(list)->int"""
    matriz1=list.plit(matriz)
    a=[]
    for i in range(len(matriz1)):
        b=str.find(numero,matriz1)
        if b!=0:
            a+=[b]
    return len(a)