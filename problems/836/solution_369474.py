def busca(setor, matriz):
    """buscar em uma matriz um respectivo setor;
    string, matriz, -> matriz"""
    m = matriz
    l = []
    for i in range(len(m)):
        if m[i][2] == setor:
            list.append(l, m[i])
    return l