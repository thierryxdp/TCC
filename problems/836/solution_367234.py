def busca(setor_busca, matriz):
    """dado um nome de um setor, retorna os dados de todos os funcionarios desse setor de busca"""
    dados = []
    for nome, registro, setor, telefone in matriz:
        if setor == setor_busca:
             dados.append([nome, registro, telefone])
    return dados