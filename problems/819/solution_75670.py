def filtraMultiplos(lista,n):
    """essa função recebe uma lista e um número N e retorna quantos elementos da lista são divisíveis por N;
    list,int-->list"""
    I=[]
    i=0
    while i<len(lista):
        if lista[i]*n==0:
            I.insert(i,lista[i])
        i=i+1
    return I