def colisao(A,B):
    '''Retorna True caso haja colisão entre dois retângulos.
    Isira as coordenadas do vértice inferior esquerdo e superior direito,
    respectivamente, dos dois retângulos.
    tupla, tupla -> bool'''
    if A[2] and A[3] < B[0] and B[1]:
        return False
    if A[0] and A[1] > B[2] and B[3]:
        return False
    else:
        return True