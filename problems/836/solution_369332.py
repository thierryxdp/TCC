def busca(setor, matriz):
    '''Busca pelo setor especifico e retorna uma lista com as informações dos membros do setor
    str, list -> list'''
    lista = []
    for x in matriz:
        if x[2] == setor:
            del x[2]
            lista.append(x)
    return lista