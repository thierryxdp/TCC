def filtraMultiplos (lista,n):
    '''dado uma lista de números e um número n, retorna a lista anterior
    apenas com os múltiplos de n; list,int->list'''
    b=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            b=b+lista[i]
        i=i+1
    return b