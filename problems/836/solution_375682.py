def busca(setor,matriz):
    '''Recebe uma matriz contendo informações do quadro de funcionários
    de uma empresa e um setor dessa empresa e retorna todos os 
    funcionários do setor buscado. (str, list -> list)'''
    informacoes = []
    for linha in matriz:
        if linha[2] == setor:
            informacoes = list.append(informacoes,(linha[0:1]+linha[2:])
    return informacoes