def faltante(listaDePecas):
    iteracoes = 1
    listaDePecas.sort()
    tamanho = len(listaDePecas) + 1
    while iteracoes <= tamanho:
        if (listaDePecas.count(iteracoes) == 0):
            return iteracoes
        iteracoes += 1