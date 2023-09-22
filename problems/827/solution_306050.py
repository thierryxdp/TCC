def qtd_divisores(x):
    '''Calcula o número de divisores do número x.
    int -> int'''
    soma=0
    n=1
    for i in range(x):
        if (x%n)==0:
            soma = soma+1
            n=n+1
    return soma