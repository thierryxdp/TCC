def faltante(lista):
    '''
    	Funcao que recebe uma lista e retorna o numero que 
        falta
        list -> int
    '''
    lista.sort()
    if 1 not in lista:
        return 1
    if lista[-1] < len(lista) + 1:
        return lista[-1] + 1
    
    i = 0
    numero = 0
    while i < len(lista):
        if lista[i+1] - lista[i] != 1:
            numero += lista[i+1] - lista[i]
    return numero