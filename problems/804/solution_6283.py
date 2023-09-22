def filtragem(tupla):
    '''função que retorna apenas os números pares de uma tupla:tupla->tupla'''
    tv = ()
    
    if tupla[0]%2 == 0:
        tv=tv+(tupla[0],)
    if tupla[1]%2 == 0:
        tv=tv+(tupla[1],)
    if tupla[2]%2 == 0:
        tv=tv+(tupla[2],)
    if tupla[3]%2 == 0:
        tv=tv+(tupla[3],)
        
    return tv