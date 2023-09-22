def qtd_divisores(n):
    ''' funcao que calcula divisores entre 1 e n
int -> int'''
    div = 0
    for i in range(n+1):
        if (n%(i+1)==0):
            div = div +1
    return div