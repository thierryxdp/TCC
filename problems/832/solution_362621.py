def eh_quadrada(mat):
    linha = len(mat)
    for i in range(linha):
        for j in range(linha[i]):
            if i == j:
                return 'True'
            else:
                return 'False'