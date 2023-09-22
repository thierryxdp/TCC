#Start your python function here
def filtra_pares(t):
    ''' docs
        tipos --> tipo '''
    tupla_nova = tuple()
    
    #--- verifico quais números são pares
    if x1 % 2 == 0:
        tupla_nova = tupla_nova + (t[0],)
        
    if x2 % 2 == 0:
        tupla_nova = tupla_nova + (t[1],)
        
    #--- finalmente retorno ao resultado
    return tupla_nova