def media_matriz(m):
    """retorna a media dos elemenyos de uma matriz"""
    m == list.range(m)
    soma = sum(m)
    return round(soma/(len(m)*len(m[0])), 2)