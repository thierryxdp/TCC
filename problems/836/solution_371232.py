lista3 = []
def busca_setor(matriz, i):
    return matriz[2]
    
def forma_lista(lista, setor):
    posicao = []
    for i in range(len(lista)):
        if lista[i] == setor:
            list.append(posicao, i)
    if len(posicao) == 0:
        return []
    else:
        return posicao
    
def busca(setor, matriz):
    lista1 = list(map(busca_setor, matriz, range(len(matriz))))
    if len(lista1) == 0:
        return []
    else:
        lista2 = forma_lista(lista1, setor)
    for i in range(len(lista2)):
        a = int(lista2[i])  
        list.append(lista3, matriz[a])
        list.remove(lista3[i], setor)
    return lista3