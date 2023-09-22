def qtd_divisores(numero):
    ''' conta quantos divisores um numero em;
    int->int'''
    n_divisores=0
    for n in range(numero):
        if numero%(n+1)==0:
            n_divisores+=1
    return n_divisores