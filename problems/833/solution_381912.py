def conta_numero(numero,matriz):
    '''recebe e retorna o numero de vezes que o num escolhido aparece na matriz
    int, list -> int'''
    
    repeticoes = 0
    
    for i in range(len(matriz)):
        if matriz.count(numero) != 0:
            repeticoes = repeticoes + matriz.count(numero)
            
        for j in range(len(matriz[i])):
            if matriz.count(numero) != 0:
                repeticoes = repeticoes + matriz[j].count(numero)
                
    return repeticoes