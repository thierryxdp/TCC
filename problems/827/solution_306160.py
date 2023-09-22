def qtd_divisores(n):
    '''Função que mostra os divisores de um numero
int -> list'''
    divlist = []
    i = 1
    while i <= n:
        if n % i == 0:
            list.append(divlist, i)
        i += 1
    return divlist