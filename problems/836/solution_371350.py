def busca(Procurar, Matriz):
    lista = []
    for linha in Matriz:
        if Procurar in linha:
            linha.remove(Procurar)
            lista += [linha]
    return lista