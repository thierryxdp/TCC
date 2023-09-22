def busca(setor, matriz):
    ''' função que recebe uma matriz com nome,registro, setor e
        telefone dos funcionários, de modo que ao indicar um setor
        a função retorna todos os dados compilados com essa descrição,
        caso haja
        [str,list-->list]'''

    COMPATIVEIS = []

    for sublista in matriz:
        if sublista[2] == setor:
            sublista = [sublista[0],sublista[1],sublista[3]]
            COMPATIVEIS += sublista
    return COMPATIVEIS