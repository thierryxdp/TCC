def busca(setor_busca, M):
    dados = []
    for nome, registro, setor, fone in M:
        if setor == setor_busca:
             dados.append([nome, registro, fone])
    return dados