def media_matriz(mat):
    """doc"""
    elementos = []
    for linha in mat:
        for elem in linha:
            elementos.append(elem)
    media = round((sum(elementos) / len(elementos)),2)
    return media