def media_matriz(m):
    """retorna a media dos elemenyos de uma matriz"""
    soma = []
    for t in m:
        for i in range(len(t[1])):
            if i == len(soma):
                soma.append(0)
            soma[i] += t[1][i]
    return soma