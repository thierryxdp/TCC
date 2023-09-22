#Start your python function here
def filtra_pares(x: tuple) -> tuple:
    '''Retorna uma nova tupla somente com os elementos pares na ordem em
    que foram inseridos.'''
    string_auxiliar = ''
    if x[0]%2==0:
    	string_auxiliar += str(x[0])
    if x[1]%2==0:
        string_auxiliar += str(x[1])
    if x[2]%2==0:
       	string_auxiliar += str(x[2])
    if x[3]%2==0:
    	string_auxiliar += str(x[3])
   	return tuple(string_auxiliar)