def busca(setor,matriz):
    '''Recebe uma matriz contendo informações do quadro de funcionários
    de uma empresa e um setor dessa empresa e retorna todos os 
    funcionários do setor buscado. (str, list -> list)'''
    informacoes = []
    for linha in matriz:
        if setor in linha:
            del(linha[2])
            informacoes = list.append(informacoes,linha)
    return informacoes