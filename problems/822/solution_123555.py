def repetidos(lista):
    '''A função retornará a quantidade de vezes que um número é igual ao seu número seguinte.
    Dados de entrada -> list
    Dados de saída -> int'''
    Q = len(lista)
    i = 0
    repeticoes = 0
    
    while i < Q:
        if lista[i-1] == lista[i]:
            repeticoes = repeticoes + 1
        i = i +1
        
    return repeticoes