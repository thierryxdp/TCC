def qtd_divisores(numeros):
    '''função que retorna quantos divisores apresenta determinado número; int => int'''
    ndd=0
    for n in range(1,numeros+1):
        if numeros % n == 0:
            ndd=ndd+1
    return ndd