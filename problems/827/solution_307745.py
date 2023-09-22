def qtd_divisores(n):
    """ Dado um número "n", retorna a 
    quantidade de divisores dele
    int -> int"""
    tudo = 0
    for contador in range(1,n+1):
        if n%contador == 0:
            tudo+= 1
    return tudo