def melhor_volta(matriz):
    '''retorna o corredor, o melhor tempo e o 
    numero da volta; list -> tuple'''
    j=0
    i=0
    l1=[]
    l2=[]
    for j in range(len(matriz)):
        l1=l1+[min(matriz[j])]
        l2=l2+[list.index(matriz[j],min(matriz[j]))]
    return list.index(l1,min(l1))+1,min(l1),l2[list.index(l1,min(l1))]+1