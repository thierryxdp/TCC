def eh_quadrada(matriz):
    "dada uma matriz, retorna booleano se a mesma for quadrada"
    linhas = 0
    colunas = 0
    for linha in matriz:
        for elemen in linha:
            colunas +=1
    return len(matriz) == colunas