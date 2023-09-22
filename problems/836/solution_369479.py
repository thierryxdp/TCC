def busca(setor, matriz):
    """buscar em uma matriz um respectivo setor;
    string, matriz, -> matriz"""
    m = matriz
    l = []
    for i in range(len(m)):
        if m[i][2] == setor:
            a = m[i]
            a = a.pop(2)
            list.append(l, a)
    return l