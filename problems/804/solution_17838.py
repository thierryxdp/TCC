def filtra_pares(tupla):
'''Retorna uma nova tupla contendo apenas os elementos pares da tupla original.'''
    nova_tupla = tuple()
    if (tupla[0]%2) ==0:
        nova_tupla = nova_tupla + (t[0],)
    
    if (tupla[1]%2) ==0:
        nova_tupla = nova_tupla + (t[1],)
      
    if (tupla[2]%2) ==0:
        nova_tupla = nova_tupla + (t[2],)
      
    if (tupla[3]%2) ==0:
        nova_tupla = nova_tupla + (t[3],)
    
    return nova_tupla