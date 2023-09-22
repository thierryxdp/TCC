def busca(setor_busca, matriz):
    dados = []
    for nome, registro, setor, fone in matriz:
        if setor == setor_busca:
             dados.append([nome, registro, fone])
    return dados 

print(busca('Contabilidade'))