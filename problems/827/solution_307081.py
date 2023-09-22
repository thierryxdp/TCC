def qtd_divisores(numeros):
    '''funcao que retorna a quantidade de numeros divisores de um determinado numero.'''
    '''int=>int'''
    ndd=0
    for n in range(1,numeros+1):
        if numeros % n==0:
            ndd=ndd+1
    return ndd