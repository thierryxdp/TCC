lista3 = []
def busca_setor(matriz, i):
    return matriz[2]
    
def forma_lista(lista, setor):
    posicao = []
    for i in range(len(lista)):
        if lista[i] == setor:
            list.append(posicao, list.index(lista, setor))
    if len(posicao) == 0:
        return []
    else:
        return posicao
    return posicao
    
def busca(setor, matriz):
    lista1 = list(map(busca_setor, matriz, range(len(matriz))))
    if len(lista1) == 0:
        return []
    else:
        lista2 = forma_lista(lista1, setor)        
    for i in range(len(lista2)):
        list.append(lista3, matriz[lista2[i]])
        list.remove(lista[i][2], lista3)
    return lista3