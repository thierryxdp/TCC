def busca(setor,dados):
    """Dado um setor e uma matriz de dados de funcionários
    (nome,registro,setor, telefone), a função retorna os
    dados de todos os funcionários desse setor."""

    funcionarios= []
    linhas = len(dados)
    colunas = len(dados[0])
    
    for i in range(linhas):
        if dados[i][2] == setor:
            funcionarios += [dados[i][0], dados[i][1], dados[i][3]]
    
    return funcionarios