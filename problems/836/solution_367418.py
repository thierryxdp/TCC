def busca(string,matriz):
    lista = []
    stringMenor = string.lower()
    for i in range(len(matriz)):
        setorMenor = matriz[i][2].lower()
        if setorMenor == stringMenor:
            info = matriz[i].pop(2)
            lista.append(matriz[i])
    return lista