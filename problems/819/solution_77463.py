def filtraMultiplos(lista,n):
    '''A função receberá como entrar uma lista de numeros e retornará apenas os números multiplos de (n).
    Dados de entrada -> list, int
    Dados de saída -> list'''
    Q = len(lista)
    i = 0
    multiplos = []
    
    while i < Q:
        if lista[i] % n == 0:
            list.append(multiplos,lista[i])
        i = i +1
        
    return multiplos