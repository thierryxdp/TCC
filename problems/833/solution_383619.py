def conta_numero (numero, matriz):
    """Função que, dado um número e uma matriz, retorna quantas vezes o número aparece na matriz.
    Entrada: int e lista.
    Saída: int."""
    
    contador = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if matriz[i][j] == numero:
                contador = contador + 1
    return contador