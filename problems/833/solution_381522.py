def repetidos(num,matriz):
    """Para que seja retornado a quantidade de repetições de um
    número indicado, digite;
    int->int"""
    contador=0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == num:        
        contador += 1
    return contador