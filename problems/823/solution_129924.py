def faltante(lista):
    '''Encontra o número faltante em uma lista
    ordenada de números inteiros;
    list -> int'''
    if lista[0] == 2:
        return 1
    incremento = +1
    if lista[0] > lista[-1]:
    	incremento = -1
    lista_completa = list(range(lista[0], lista[-1] + incremento))
    if not list(set(lista_completa) - set(lista)):
		return lista[-1] + incremento   
    return list(set(lista_completa) - set(lista))[0]