#Start your python function here
def filtra_pares(tupla):
    
    primeiro=tupla[0]
    segundo=tupla[1]
    terceiro=tupla[2]
    quarto=tupla[3]
    nova_tupla=('nada ainda',)
    
    if   primeiro%2==0:
        nova_tupla=nova_tupla+( primeiro ,)
    if   segundo%2==0:
        nova_tupla=nova_tupla+( segundo ,)
    if   terceiro%2==0:
        nova_tupla=nova_tupla+( terceiro ,)
    if   quarto%2==0:
        nova_tupla=nova_tupla+( quarto ,)
    return nova_tupla[1:]