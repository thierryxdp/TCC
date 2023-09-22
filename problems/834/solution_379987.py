def media_matriz(A):
    '''
    	A função recebe uma matriz de números inteiros não vazia e retorna a média
        entre os números da matriz, com duas casas decimais de precisão.
        A -> list (matriz de números inteiros não nula)
        list -> float
    '''
    r = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            r += A[i][j]
   	r /= len(A)*len(A[0])
    return round(r,2)