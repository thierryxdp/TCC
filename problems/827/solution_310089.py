def qtd_divisores(n):
    '''Calcula a quantidade de divisores de um número 'n'.
    int->int'''
    i=0
    for x in range(n):
        if n%(x+1)==0:
            i=i+1
    return i