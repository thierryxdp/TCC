def eh_quadrada(matriz):
    linhas = 0
    coluna = 0
    for lista in matriz:
        for itens in lista:
            coluna = coluna + 1
        linhas = linhas + 1
    if linhas == coluna:
        return True
    else:
        return False