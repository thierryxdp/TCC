def busca(matriz, setor):
    """buscar em uma matriz um respectivo setor;
    matriz, strin, -> matriz"""
    m=matriz
    l = []
    for i in range(len(m)):
        if m[i][2] == setor:
            list.append(l, m[i])
    return l