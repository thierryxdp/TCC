def busca(setor,matriz):
    """A função retorna dados de todos os funcionários de um determinado
    setor.
    str-->list"""
    lista = []
    #percorrer e achar os contatos com o setor desejado
    for x in range(len(matriz)):
        if setor in matriz[x]:
            lista.append(matriz[x])
    #retirar o setor
    for y in range(len(lista)):
        if lista.append[y][2] == setor:
            del lista[y][2]
    return lista