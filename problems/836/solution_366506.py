def busca (setor, lista):
    lista2 = []
    for a in range(len(lista)):
        if lista[a][2] == setor:
            lista2 = lista
    return lista2