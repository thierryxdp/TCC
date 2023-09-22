def eh_quadrada(matriz):
    "dada uma matriz, retorna booleano se a mesma for quadrada"
    linha = 0
    coluna = 0
    for linha in matriz:
        for elemen in linha:
            coluna +=1
        linha += 1
    return linha == coluna