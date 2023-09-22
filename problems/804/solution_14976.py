def filtra_pares(tupla):
    """ Recebe uma tupla com 4 elementos inteiros como parâmetro, e retorna uma nova tupla contendo apenas 
    os números pares da tupla original, na mesma ordem em que se encontravam"""
    a,b,c,d=tupla
    resultado=0,
    if a%2== 0:
        a=(a,)
        resultado=resultado+a
    if b%2 ==0:
        b=(b,)
        resultado=resultado+b
    if c%2 ==0:
        c=(c,)
        resultado=resultado+c
    if d% 2 ==0:
        d= (d,)
        resultado= resultado+d
    return resultado [1:]