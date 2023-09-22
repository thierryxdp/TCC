def repetidos(lista):
    """"Esta função recebe uma lista e retorna a quantidade de vezes em que um elemento da lista é igual ao anterior.
    list -> int"""
    l = []
    descarte = []
    for i in lista:
        if i == l[-1]:
            descarte.append(i)
        else:
        	l.append(i)
	return len(lista) - len(l)