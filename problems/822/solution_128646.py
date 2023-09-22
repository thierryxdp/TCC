def repetidos (lista):
    '''Retorna quantas vezes numa lista dois números consecutivos são iguais, lista -> int'''
    lista1 = []
    for element in lista:
    	if element not in lista1:
        lista1.append(element)
    return len(lista1)