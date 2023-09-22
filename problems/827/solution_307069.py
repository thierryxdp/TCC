def qtd_divisores(n):
    '''Função que retorna a quantidade de divisores de um número. int->int'''
    divisores = ()
    for a in range(1,n+1):
        if n%a == 0:
            divisores = divisores + (a,)
    return len(divisores)