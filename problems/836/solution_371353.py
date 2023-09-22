def busca(setor,matriz):
    """ Dada uma matriz 3x4 com dados armazenados em forma de string dentro dela, dado um setor x, retorna os dados de daquele setor;
    string,lista->lista """
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            lista.append(matriz[i])
    for i in range(len(lista)):
        lista[i].remove(setor)
    return lista