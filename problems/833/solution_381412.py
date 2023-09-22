def conta_numero(num,matriz):
    """Função que calcula a qauntidade de vezes que se repete um nmuero dentro de uma matriz dados de entrada e retorna a quantidade de vezes
    int , list -> int"""
    total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == num:
                total = total +1
    return total