def busca(matriz):
    """retorna os dados do setor"""
    dados = []
    for nome, registro, setor, telefone in matriz:
        if setor == setor_busca:
             dados.append([nome, registro, telefone])
    return dados