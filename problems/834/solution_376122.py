def media_matriz(m):
    """retorna a media dos elementos da matriz"""
    soma = 0
    for i in m:
        soma = soma + i
    return soma/(len(m)*len(m[0]))