def fatorial(n):
    """ Função que dado um número, calcula seu fatorial
    int -> int """
    cont=1
    i=2
    while i<=n:
        cont = cont*i
        i+=1
    return cont