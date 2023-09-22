def busca(setor,lista):
    dados = []
    for pessoa in lista:
        if setor in pessoa:
            pessoa.pop(2)
            dados.append(pessoa)
    return dados