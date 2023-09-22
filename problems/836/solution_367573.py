def busca(setor,matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    funcionario = 0
    funcionarios = []
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] == setor:
                funcionario = del(matriz[i],j)
                funcionarios = funcionarios + funcionario
    return funcionarios