def filtra_pares(algorismo):
    '''calcule uma função que receba uma tupla com quatro elementos inteiros, e retorne uma nova tupla contendo apenas os elementos pares da tupla original. tupla-->tupla.'''
    a = algorismo[0]
    b = algorismo[1]
    c = algorismo[2]
    d = algorismo[3]
    tupla_final = ()
    if a%2 == 0:
        tupla_final = tupla_final + (a,)
    if b%2 == 0:
        tupla_final = tupla_final + (b,) 
    if c%2 == 0:
        tupla_final = tupla_final + (c,) 
    if d%2 == 0:
        tupla_final = tupla_final + (d,) 
        
    return tupla_final