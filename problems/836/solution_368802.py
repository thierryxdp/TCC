def busca(setor, matriz):
    """função que recebe o nome do setor e uma matriz de
    4 elementos contendo informações dos funcionarios de
    uma empresa e retorna todas as informações de todos os
    funcionário daquele setor.
    str,list-> list"""

    lista = []

    for linha in matriz:
        if linha[2] == setor:
                lista += [linha]

    return lista