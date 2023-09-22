def colisao(A,B):
    '''Retorna True caso haja colisão entre dois retângulos.
    Isira as coordenadas do vértice inferior esquerdo e superior direito,
    respectivamente, dos dois retângulos.
    tupla, tupla -> bool'''
    if A[2] < B[0]:
        return False
    if A[0] > B[2]:
        return False
    if A[1] > B[3]:
        return False
    if A[3] < B[1]:
        return False
    else:
        return True