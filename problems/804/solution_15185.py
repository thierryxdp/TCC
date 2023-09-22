def filtra_pares(algorismo):
    '''calcule uma função que receba uma tupla com quatro elementos inteiros, e retorne uma nova tupla contendo apenas os elementos pares da tupla original. tupla-->tupla.'''
    a = algorismo[0]
    b = algorismo[1]
    c = algorismo[2]
    d = algorismo[3]
    ultima_tupla = ()
    if a%2 == 0:
        ultima_tupla = ultima_tupla + (a,)
    if b%2 == 0:
        ultima_tupla = ultima_tupla + (b,) 
    if c%2 == 0:
        ultima_tupla = ultima_tupla + (c,) 
    if d%2 == 0:
        ultima_tupla = ultima_tupla + (d,)    
    return ultima_tupla