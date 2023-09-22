def faltante(L):
    '''função que recebe uma lista com N-1 inteiros numerados de 1 a N como entrada e retorna qual inteiro está faltando nesse intervalo; list -> int'''
    i=0
    list.sort(L)
    while i<len(L):
        if len(L)==1 and 3>L[0]>1:
            x=L[0]-1
            return x
        if L[i]+1 not in L: 
            x= L[i]+1
            return x
        if L[i]-1 not in L and L[i]>1:
            x=L[i]-1   
            return x    
        i=i+1