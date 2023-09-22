def filtra_pares (tupla):
    
    'Funcao que recebe uma tupla com quatro elementos inteiros como
	'parametro e retorna uma nova tupla contendo apenas os elementos
	'pares da tupla original, na mesma ordem em que se encontravam'
    
    pares = ()
    
    if tupla [0] % 2 == 0:
        pares = pares + (tupla [0], )
    if tupla [1] % 2 == 0:
        pares = pares + (tupla [1], )
    if tupla [2] % 2 == 0:
        pares = pares + (tupla [2], )
    if tupla [3] % 2 == 0:
        pares = pares + (tupla [3], )