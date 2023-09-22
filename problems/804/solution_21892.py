def filtra_pares (a,b,c,d):
    '''função que dados quatro elentos inteiros retorne quais deles são pares
     na mesma ordem em que já haviam sido informados.
     int, int, int, int -> tuple'''
    saida=()
    if a%2==0:
        saida+=(a,)
    if b%2==0:
        saida+=(b,)
    if c%2==0:
        saida+=(c,)
    if d%2==0:
        saida+=(d,)
    return saida