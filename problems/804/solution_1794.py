#Start your python function here
def filtra_pares(tupla):
    """Funcao que retorna uma tupla feita somente de numeros pares, com base
    em uma tupla escolhida."""
    
    a, b, c, d = tupla
    nova_tupla = ()
    
    if(a%2 == 0):
        nova_tupla = nova_tupla + (a,)
    if(b%2 == 0):
        nova_tupla = nova_tupla + (b,)
    if(c%2 == 0):
        nova_tupla = nova_tupla + (c,)
    if(d%2 ==0):
        nova_tupla = nova_tupla + (d,)
    return nova_tupla