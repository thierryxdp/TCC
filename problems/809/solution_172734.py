"""Recebe duas listas de 3 elementos e retorna uma terceira lista com os 
elementos recebidos intercalados"""
"""list->list"""
def intercala(lista1, lista2):
	l3 = []
	l3.append(lista1[0])
    l3.append(lista2[0])
	l3.append(lista1[1])
    l3.append(lista2[1])
	l3.append(lista1[2])
	l3.append(lista2[2])
	return l3