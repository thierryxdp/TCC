def busca(setor, matriz):
    '''funçao que retorna  dados  de  todos  os funcionários
    de um determinado  setor
    str-->list '''

    dados = []

    for i in range(len(matriz)):
        if setor in matriz[i]:
            dados.append(matriz[i])
        for j in range(len(dados)):
            if dados[j][2] == setor:
                del dados[j][2]