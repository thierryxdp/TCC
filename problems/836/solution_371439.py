def busca(setor,matriz):
    '''Dado um setor da empresa e uma lista de sub-listas que
    representa uma matriz como a exemplificada no exercício
    retorna todas as informações de todos os funcionários
    daquele setor.
    str, list -> list'''
    acumul = []
    for linha in matriz:
        if setor in linha:
            del(linha,[2])
            list.append(acumul,linha)
    return acumul