def fatorial(n):
    """ Retorna o valor de n fatorial; int -> int """
    i=1;
    fat=1
    while i<=n:
        fat=fat*i
        i+=1
    return fat;