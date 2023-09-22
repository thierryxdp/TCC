def qtd_divisores(n):
    ''' funcao recebe um numero e diz qauntos divisores esse numero tem,
    int-->int'''
    for divisor in range(1,n+1):
        if n % divisor==0:
            return divisor