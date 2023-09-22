#Start your python function here
#int, int, int, int --> int
def filtra_pares(tupla):
    """Agrupa somente os elementos pares provenientes dos parâmetros na 
       mesma ordem em que se encontravam.
       Dados de entrada: tupla --> possuindo vários números inteiros"""
    if tupla[0] % 2 == 0:
    	newtupla = (tupla[0],)
    else:
        newtupla = ()
    if tupla[1] % 2 == 0:
    	newtupla1 = (tupla[1],)
    else:
        newtupla1 = ()
    if tupla[2] % 2 == 0:
    	newtupla2 = (tupla[2],)
    else:
        newtupla2 = ()
    if tupla [3] % 2 == 0:
    	newtupla3 = (tupla[3],)
    else:
        newtupla3 = ()
    return newtupla + newtupla1 + newtupla2 + newtupla3