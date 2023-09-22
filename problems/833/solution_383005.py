def conta_numero(numero, matriz):
    """Dado um número inteiro e uma matriz de inteiros retorna quantas vezes
       o número dado aparece na matriz.
       int list -> int"""
    
    soma = 0
    
    for i in len(matriz):
        pivo = matriz[indice1]
        
        for j in len(pivo):
            if pivo[indice2] == numero:
                soma += 1
        
    return soma