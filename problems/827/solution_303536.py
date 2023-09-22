def qtd_divisores(n):
    '''Função calcula e retorna quantos divisores um número n tem;
    int -> int'''
    div = 0
    if n <0: n = n*-1
    for  i in range(1,n+1):
        if n%i == 0:
            div += 1
    return div