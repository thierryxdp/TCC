def filtraMultiplos(lista, n):
	"""Função que filtra a lista, mantendo os números que são multiplos do número n;
list, int -> list"""
multiplos = []
for elemento in lista:
    if elemento%n == 0:
        list.append(multiplos, elemento)
       return multiplos