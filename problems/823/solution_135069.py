def faltante(L):
    '''função que recebe uma lista L contendo n-1 números inteiros, não
    necessariamente em ordem crescente, numerados com valores de 1 até N sem 
    repetição de valores, retorna o número inteiro que pertence ao intervalo
    [1,N] que não pertence à lista L; list->int'''
    
    ordenada=L
    list.sort(ordenada)
    i=1
    
    if ordenada[0]!=1:
        return 1
    
    while i<len(ordenada):
        if ordenada[i]!=ordenada[i-1]+1:
            return ordenada[i]-1
        i=i+1
    
    return len(ordenada)+1