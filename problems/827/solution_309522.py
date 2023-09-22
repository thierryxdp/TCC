def qtd_divisores(n):
    '''Função que dado um número (n) conta quantos divisores esse número possui;
       int->int'''
    divisores = 0
    for i in range(1,n+1):
        if n%i==0:
            divisores = divisores + 1
    return divisores