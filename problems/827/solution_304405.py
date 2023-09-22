def qtd_divisores(x):
    '''funcao conta o numero de divisores que tem o numero determinado na entrada'''
    contador = 0
    for i in range(1, x+1):
        if ((x % i) == 0):
            contador +=1
    return contador