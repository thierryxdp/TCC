def filtra_pares(t):
    '''funçao que retorna uma tupla com os numeros pares
    de uma tupla de entrada'''
    a=t[0]
    b=t[1]
    c=t[2]
    d=t[3]
    tupla_final = ()
    if a%2 == 0:
        tupla_final=tupla_final+(a,)
    if b%2 == 0:
        tupla_final=tupla_final+(b,)
    if c%2==0:
        tupla_final=tupla_final+(c,)
    if d%2==0:
        tupla_final=tupla_final+(d,)
    return tupla_final