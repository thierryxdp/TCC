def media_matriz(m):
    """retorna a media dos elemenyos de uma matriz"""
    soma = [0]*2
    for t in m:
        soma[0] += t[1][0]
        soma[1] += t[1][1]
    return soma