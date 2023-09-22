#Start your python function here
def filtra_pares(t):
    ''' função que retorna umatupla contendo apenas elementos pares da dupla original 
    tupla, int '''
    nova_tupla = tuple()
    if (t[0]//2) == 0: 
     nova_tupla = nova_tupla + (t[0],)
    if (t[1]//2) == 2:
     nova_tupla = nova_tupla + (t[1],)
    if (t[2]//2) == 4:
     nova_tupla = nova_tupla + (t[2],)
    if (t[3]//2) == 6:
     nova_tupla = nova_tupla + (t[3],)