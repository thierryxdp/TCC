def qtd_divisores(n):
    '''Calcula e retorna a quantidade de divisores que o número n tem.
    int-->int'''
    qtd=0
    for i in range(1,n+1):
        if n%i==0:
            qdt=qtd+1
    return qtd