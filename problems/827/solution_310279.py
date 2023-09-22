def qtd_divisores (i):
    '''Calcula quantos divisores tem um inteiro i, int->int'''
    divisores = []
    for elemento in range(i):
        if i%elemento==0 and elemento!=0:
        divisores = divisores + [elemento]
    return len(divisores)