def busca(setor,matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    funcionarios = []
    for i in range(linha):
        if matriz[i][2] == setor:
            pessoa = []
            for j in range(coluna):
                if matriz[i][j] != setor:
                    pessoa.append(matriz[i][j])
                funcionarios.append(pessoa)
    return funcionarios