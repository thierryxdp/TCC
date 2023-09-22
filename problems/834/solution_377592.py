def media_matriz(matriz):
    """Função que dada a matriz da entrada retorna a media de todos os numeros da matriz; int-> float"""
    n_mat=0
    n=0
    for i in matriz:
        n_mat=n_mat+sum(i)
        n=n+len(i)
    return n_mat/n