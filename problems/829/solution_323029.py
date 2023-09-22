def soma_h(numero):
    '''recebo um numero inteiro que calcula o valor de H que contém N termos.
int -->float'''
    contador=0
    for x in range(1,numero+1):
        h = 1/ x
        contador +=h
    return hound(contador,2)