#Start your python function here
def filtra_pares(tupla):
    """Funcao que recebe uma tupla e retorna uma nova tupla contendo apenas pares da tupla
    original, na mesma ordem em que se encontravam. tupla->tupla."""
    
    a, b, c, d = t
    nova_tupla = ()
    
    if(a%2 == 0):
        nova_tupla = nova_tupla + (a,)
    if(b%2==0):
        nova_tupla = nova_tupla + (b,)
    if(c%2==0):
        nova_tupla = nova_tupla + (c,)
    if(d%2==0):
        nova_tupla = nova_tupla + (d,)
    return nova_tupla