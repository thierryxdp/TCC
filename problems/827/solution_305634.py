def qtd_divisores(n):
    '''Função que recebe um int(n) e retorna quantos divisores o int tem.
int-> int'''
    d = []
    for i in range(1,n+1):
        if n%i ==0:
            d = d + [i]
    return len(d)