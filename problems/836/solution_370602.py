def busca(setor, matriz):
    dados = []
    for funcionario in matriz:
        if setor in funcionario[2]:
            list.append(dados,funcionario[:2]+[funcionario])
    return dados