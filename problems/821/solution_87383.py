def fatorial(num):
    '''Função que dado um número (num) retorna o seu fatorial.
    int->int'''
    
    i=1
    fatorial_num= 1

    while i<=num:
        fatorial_num= fatorial_num*i
        i=i+1

    return fatorial_num