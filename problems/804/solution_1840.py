def filtra_pares(tupla):
    """ dada uma tupla de quatro números inteiros, a função
retorna uma nova tupla contendo apenas os números pares
da tupla original.
tupla-->tupla
        
Parâmetros
tupla: tupla com quatro elementos inteiros (a,b,c,d)
"""
    a,b,c,d=tupla
    nova=()
    if a%2==0:
        a=(a,)
        nova=nova+a
    if b%2==0:
        b=(b,)
        nova=nova+b
    if c%2==0:
        c=(c,)
        nova=nova+c
    if d%2==0:
        d=(d,)
        nova=nova+d
    return nova
    
    return x