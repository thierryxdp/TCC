def media_matriz(m):
    """retorna a media dos elemenyos de uma matriz"""
    soma = sum(m[0])+sum(m[1])+sum(m[2])
    return soma/(len(m)*len(m[0]))