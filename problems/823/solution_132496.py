def faltante(lista):
	'''descobre qual o numero inteiro do intervalo da lista que está faltando'''
    lista.sort()
    n = len(lista) + 1
    inteiroFaltante = 0
   	i = 0
    
    while i in range(n):
        if(i == len(lista):
           inteiroFaltante = i
        if(lista[i + 1] - lista[i] > 1):
            inteiroFaltante = lista[i] - 1
        i = i+1
    return inteiroFaltante