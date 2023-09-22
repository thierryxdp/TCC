#Start your python function here
def filtra_pares(numeros):
    '''Função que recebe uma tupla com quatro elementos inteiros, e retorne uma nova tupla contendo apenas os elementos pares da tupla original.
    tuple -> tuple'''
    pares = ()
    if numeros[0] % 2 == 0:
        pares = pares + (numeros[0],)
    if numeros[1] % 2 == 0:
        pares = pares + (numeros[1],)
    if numeros[2] % 2 == 0:
        pares = pares + (numeros[2],)
    if numeros[3] % 2 == 0:
        pares = pares + (numeros[3],)
	return pares