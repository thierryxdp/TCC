#Start your python function here
def filtra_pares(tupla):
    """ Funcao recbe uma tupla com quatro elementos inteiros e retorna uma
    nova tupla com apenas os elemtnos pares da tupla original, na mesma
    ordem em que se encontravam """
    
    t = (x1,x2,x3,x4)
    
    if tupla[0]%2 == 0:
        x1 = tupla[0]
    else:
        x1 = ()
    
    if tupla[1]%2 == 0:
        x2 = tupla[1]
    else:
        x2 = ()
        
    if tupla[2]%2 == 0:
        x3 = tupla[2]
    else:
        x3 = ()
    
    if tupla[3]%2 == 2:
        x4 = tupla[3]
    else:
        x4 = ()
    
    return t