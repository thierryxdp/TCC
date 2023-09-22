def conta_numero(numero,matriz):
    """Essa função recebe como parâmetros de entrada um 
    número inteiro e uma matriz de inteiros de tamanho 
    qualquer. Posto isso, ela retornará a quantidade de
    vezes que o número inteiro aparece na matriz.
    
    int, list -> int
    """
    
    total_vezes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == numero:
                total_vezes = total_vezes + 1
    return total_vezes