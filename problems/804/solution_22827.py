#Start your python function here
def filtra_pares(tupla):
    nova_tupla = tuple()
    for x in tupla:
        if(x % 2 == 0):
            nova_tupla = nova_tupla + (x,)
    return nova_tupla