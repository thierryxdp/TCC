def filtraMultiplos(lista, num):
    '''
    	Função que recebe que recebe uma lista e um número e retorna uma lista
        contendo os números da devida lista que são seus multiplos.
        list, int -> list
    '''
    i=0
    resultado = []
    while i < len(lista):
        if lista[i]%num == 0:
            resultado.append(lista[i])
    return result