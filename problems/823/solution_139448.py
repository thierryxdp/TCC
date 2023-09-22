def faltante(L):
    '''função que recebe uma lista l de tamanho n-1 e retorna qual
    número pertence ao intervalo [i,n] mas não a lista l
    list->int'''
    
    i=0
    menor=min(L)
    maior=max(L)
    numeros=[]
    
    while i<len(L):
        if i!=maior and i!=menor:
            if i+1 not in L or i-1 not in L:
                numeros=numeros+L[i]
    i=i+1
    
    return numeros