def qtd_divisores(numero):
    ''' conta quantos divisores um numero em;
    int->int'''
    n_divisores=1
    for n in range(numero):
        if n%numero==0:
            n_divisores+=1
    return n_divisores