import collections 

def conta_numero(numero,matriz):
   '''recebe e retorna o numero de vezes que o num escolhido aparece na matriz
    int, list -> int'''
    
    repeticoes = 0
    
    for i in range(len(matriz)):
        if collections.Counter(numero) != 0:
            repeticoes = repeticoes + collections.Counter(numero)
            
        for j in range(len(matriz[i])):
            if collections.Counter(numero) != 0:
                repeticoes = repeticoes + collections.Counter(numero)
                
    return repeticoes