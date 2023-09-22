def faltante(lista):
    '''
    	Funcao que recebe uma lista e retorna o numero que 
        falta
        list -> int
    '''
    lista.sort()
    i = 0
    numero = 0
    while i < len(lista):
        if lista[i] in '123456789':