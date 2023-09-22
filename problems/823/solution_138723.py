def faltante( lista):
    '''essa funçao recebe uma lista com N-1 numeros e precisa retornar qual o numero que está faltando
lista -> int'''
    i=1
    list.sort(lista)
    
    if lista[0]!=1:
            return 1
    while i < len(lista):
        if lista[i]!=lista[i-1]+1:
            i=i+1
        
    return i+1