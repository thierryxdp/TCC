def conta_numero(numero, matriz):
    """
    Função que recebe um número inteiro e uma matriz de inteiros e retorna o número de vezes que esse número aparece na matriz.
    Parâmetros:
    	numero: int
        matriz: list
    Saída:
    	int
    """
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                contador += 1
    return contador