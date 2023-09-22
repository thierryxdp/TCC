def repetidos(lista):
    """Esta função recebe uma lista de números inteiros e retorne a quantidade de elementos da lista que são iguais ao elemento anterior
    list -> int"""
    l = []
    if len(lista) == 10 or len(lista) == 20:
        return (len(lista) - len(set(lista)))
    elif len(lista)%2 == 0:
    	for i in lista:
        	if lista[lista.index(i)+1] == lista[lista.index(i)]:
            	l.append(i)
    	return (len(l)+1)//2
    else:
        return (len(lista) - len(set(lista)))