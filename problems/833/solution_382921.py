def conta_numero(numero, matriz):
    """Dado um número inteiro e uma matriz de inteiros retorna quantas vezes
       o número dado aparece na matriz.
       int list -> int"""
    
    soma = 0
    indice1 = 0
    indice2 = 0
    
    while indice1 <= len(matriz[indice1]):
        pivo = matriz[indice1]
        
        for indice2 in range(len(pivo[indice2])):
            pivo[indice2] == numero
            soma += 1
            indice2 += 1
                
        indice1 += 1
        
    
    return soma