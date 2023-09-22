def faltante(lista_numeros):
    '''identifica qual número inteiro está faltando em uma lista com N números, numerados de 1 a N
    list -> int'''
	list.sort(lista_numeros, reverse=True)
    i = 0
    while i < len(lista_numeros):
        if lista_numeros[i] + 1 not in lista_numeros:
            return lista_numeros[i]
        i = i + 1