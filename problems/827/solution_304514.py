def qtd_divisores(n):
    '''Verifica a quantidade de divisores de um número n;
int -> int'''
    qtd = 0
    for i in range(1,n+1):
        if n%i==0:
            qtd += 1
    return qtd