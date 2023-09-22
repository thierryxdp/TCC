def conta_numero(numero,matriz):
    """
    Função recebe um numero inteiro e uma matriz de inteiros de tamanho qualquer,
    conta e retorna quantas vezes aquele número aparece na matriz.
    int, matriz -> int
    """
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero==matriz[i][j]:
                contador+=1
  	
    return contador