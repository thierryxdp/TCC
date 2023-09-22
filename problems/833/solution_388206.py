def conta_numero(numero,matriz):
    """ Função que retorna quantas vezes um número aparece
    aparece na matriz
    Entrada : int list
    Saída: int """
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                total+=1             
    return total