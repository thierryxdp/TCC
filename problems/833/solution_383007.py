def conta_numero(numero, matriz):
    """Dado um número inteiro e uma matriz de inteiros retorna quantas vezes
       o número dado aparece na matriz.
       int list -> int"""
    
    repeticoes = 0
    
    for indice1 in range(len(matriz)):
        pivo = matriz[indice1]
        
        for indice2 in range(len(pivo)):
            if pivo[indice2] == numero:
                repeticoes += 1
        
    return repeticoes