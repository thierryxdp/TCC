def melhor_volta(matriz):
    '''retorna o corredor, o melhor tempo e o 
    numero da volta; list -> tuple'''
    j=0
    i=0
    l1=[]
    for j in range(len(matriz)):
        l1=l1+[min(matriz[j])]
    return min(l1)