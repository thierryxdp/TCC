def busca(setor:str,dados:list) -> list:
    """Dado um setor e um matriz de dados de funcionários
    (nome, registro, setor, telefone), a função retorna os
    dados de todos os funcionários desse setor."""
    
    funcionarios = []
    linhas = len(dados)
    colunas = len(dados[0])
    
    for i in range(linhas):
        if dados[i][2] == setor:
            funcionario = [dados[i][0], dados[i][1], dados[i][3]]
            list.append(funcionarios, funcionario)
    
    return funcionarios