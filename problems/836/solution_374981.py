def busca(setor, matriz):
    dados = []
    for funcionario in matriz:
    linha = []    
        if setor in funcionario[2]:
            list.append(linha,funcionario[0])
            list.append(linha,funcionario[1])
            list.append(linha,funcionario[3])
        dados = dados + linha    
    return dados