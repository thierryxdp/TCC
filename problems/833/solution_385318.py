def conta_numero(numero,matriz):
    """Dado um número inteiro e uma matriz de inteiros, a
    função conta quantas vezes o número aparece na matriz
    e o retorna.
    Parametros de Entrada: int,list
    Retorna: int"""
    
    aparecimento=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero== matriz[i][j]:
                aparecimento=aparecimento+1
    return aparecimento