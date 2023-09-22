def conta_numero(numero, matriz):
    """Dado um número inteiro e uma matriz de inteiros retorna quantas vezes
       o número dado aparece na matriz.
       int list -> int"""
    
    soma = 0
    
    for indice1 in range(len(matriz[indice1])):
        pivo = matriz[indice1]
        
        for indice2 in range(len(pivo[indice2])):
            if pivo[indice2] == numero:
                soma += 1
        
    
    return soma