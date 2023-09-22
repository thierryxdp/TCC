def conta_numero(numero, matriz):
    """ Função que dado um número inteiro e uma matrizde números
        inteiros, conta e retorna quantas vezes aquele número aparece
        na matriz.
        
        Parameters:
        numero: Número inteiro que será buscado pela função
        matriz: Matriz de números inteiros
        
        Returns:
        Retorna a quantidade de vezes que o numero dado na entrada 
        aparece na matriz.
        int, list -> int"""
    quantidade = 0
    elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elementos = elementos + 1
            if matriz[i][j] == numero:
                quantidade = quantidade + 1
    return quantidade