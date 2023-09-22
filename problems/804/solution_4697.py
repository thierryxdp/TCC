#Start your python function here
def filtra_pares(x: tuple) -> tuple:
    '''Retorna uma nova tupla somente com os elementos pares na ordem em
    que foram inseridos.'''
    tupla_auxiliar = ()
    if x[0]%2==0:
    	tupla_auxiliar += (x[0],)
    if x[1]%2==0:
        tupla_auxiliar += (x[1],)
    if x[2]%2==0:
       	tupla_auxiliar += (x[2],)
    if x[3]%2==0:
    	tupla_auxiliar += (x[3],)
    return tupla_auxiliar