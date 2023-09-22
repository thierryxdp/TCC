def faltante(lista):
    '''dada uma lista com n - 1 inteiros numerados de 1 a 
    n, retorna o numero inteiro que está faltando;
    list --> int'''
    list.sort(lista)
    lista_completa = list(range(1,lista[-1]+1))
    i = 0
    while i < len(lista_completa):
        if not(lista[i] == lista_completa[i]):
            return lista_completa[i]
        i = i + 1
	return lista[-1] + 1