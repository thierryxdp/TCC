def busca(setor,matriz):
    """Recebe uma matriz e uma setor, dado o nome do setor a funçãi retorna 
    os dados dos funcionarios do setor"""
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