def qtd_divisores(n):
    '''Calcula e retorna a quantidade de divisores que o número n tem.
    int-->int'''
    qdt=0
    for i in range(1,n+1):
        if n%i==0:
            qdt=qdt+1
    return qtd