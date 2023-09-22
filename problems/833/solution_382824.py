def conta_numero(numero, matriz):
    """Dado um número inteiro e uma matriz de inteiros retorna quantas vezes
       o número dado aparece na matriz.
       int list -> int"""
    
    indice1 = 0
    indice2 = 0
    soma = 0
    
    while indice1 =< len(matriz):
        pivo = matriz[indice1]
        indice1 += 1
        
        while indice2 =< len(matriz[indice1]):
            if matriz[indice1][indice2] == numero:
                soma += 1
                
            indice2 += 1
            
    return soma