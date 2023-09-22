def busca(m):
    dados = []
    for nome, registro, setor, telefone in m:
        if setor == setor_busca:
             dados.append([nome, registro, fone])
    return dados