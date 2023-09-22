#Stdef filtra_pares(tupla):
    """dada uma tupla com 4 números inteiros, retorna uma tupla contendo
    somente os números pares da tupla, na ordem em que aparecem na tupla
    original. tuple->tuple"""
    L=()
    a,b,c,d=tupla
    if a%2==0:
        L=L+(a,)
    if b%2==0:
        L=L+(b,)
    if c%2==0:
        L=L+(c,)
    if d%2==0:
        L=L+(d,)
    return Lart your python function here