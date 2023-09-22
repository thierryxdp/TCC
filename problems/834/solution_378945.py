def media_matriz(matriz):
    """Soma a uma variável de valor inicial 0, o valor de cada elemento da matriz,
    que é usado substituindo em 'matriz[i][j]' os valores de 'i' variando de 0 até o tamanho
    da matriz, e de 'j' variando de 0 até o tamanho de um elemento da matriz.
    Após isso, divide esta variável pelo tamanho da matriz vezes o tamanho de um elemento,
    que é o número de elementos da matriz, e retorna esta divisão.
    lista-> float
    """
    soma=0
    lin=len(matriz)
    col=len(matriz[0])
    for i in range(lin):
        for j in range(col):
            soma+=matriz[i][j]
    return soma/(lin*col)