def busca(setor,matriz):
    '''Recebe uma matriz contendo informações do quadro de funcionários
    de uma empresa e um setor dessa empresa e retorna todos os 
    funcionários do setor buscado. (str, list -> list)'''
    informacoes = []
    for linha in matriz:
        for aij in linha:
            if aij == setor:
                del(linha[2])
                informacoes.extend(linha)
    return informacoes