def qtd_divisores(n):
    '''retorna a quantidade de divisores o numero n possui
    int -> int'''
    div = 0
    for num in range(1,n+1):
        if n%num == 0:
            div = div + 1
    return div