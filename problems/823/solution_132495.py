def faltante(lista):
	'''descobre qual o numero inteiro do intervalo da lista que está faltando'''
    lista.sort()
    n = len(lista)
    inteiroFaltante = 0
    i = 0
    while i < n:
        if(i != lista[i]):
            inteiroFaltante = i
        i = i + 1
    return inteiroFaltante