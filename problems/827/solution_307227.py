def qtd_divisores(n):
    ''' funcao recebe um numero e diz qauntos divisores esse numero tem,
    int-->int'''
    c=0
    for divisor in range(1,n+1):
        if n % divisor==0:
            c+= c+divisor
            return c