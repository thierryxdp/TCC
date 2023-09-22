import collections 

def conta_numero(numero,matriz):
    '''conta o numero de vezes que um certo numero inteiro se repete em uma matriz
    int, list -> list'''

    repeticoes = 0
    
    for i in range(len(matriz)):
        if collections.Counter(numero) != 0:
            repeticoes = repeticoes + collections.Counter(numero)
            
        for j in range(len(matriz[i])):
            if collections.Counter(numero) != 0:
                repeticoes = repeticoes + collections.Counter(numero)
                
    return repeticoes