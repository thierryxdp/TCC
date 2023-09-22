def busca(setor,matriz):
    '''Dado uma matriz, com as informações dos
    funcionários e o setor desejado, retorna as
    informações sobre todos os funcionários daquele
    setor.
    str, list -> list'''
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if elemento in matriz[i][j]:
                lista.append(matriz[i])
    for k in lista:
        for o in k:
            if o==elemento:
                indice=k.index(elemento)
                del k[indice]
    return lista