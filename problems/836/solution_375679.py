def busca(setor,matriz):
    """ Recebe o nome de um setor e uma matriz contendo as informaçãoes referentes a nome, registro, setor e telefone dos
    funcionarios e retorna os registros dos funcionarios do setor informado"""
    registro = []

    for informacoes in matriz:
        if informacoes[2] == setor:
            registro = registro + [[informacoes[0],informacoes[1],informacoes[3]]]

    return registro