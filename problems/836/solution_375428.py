def busca(matriz,setor):
    lista = []
    for elemento in matriz:
        if elemento[2] == setor:
            lista += elemento[0] + elemento[1]+elemento[3]
    if lista != []:
        return lista
    else:
        return