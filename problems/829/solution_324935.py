def soma_h(n):
    '''Funcao que calcula o somatorio h
    dado n numero de termos como valor de entrada'''
    s = 0
    for i in range(1,n):
        s = s + 1/(i)
    return round(s,2)