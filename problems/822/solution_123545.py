def repetidos(lista):
    """A função recebe uma lista e retorna a quantidade de
	vezes em que o elemento da lista é igual ao anterior;
	list->int"""
	
    i=0
    resultado=0
    while i+1<len(lista):
        if lista[i] == lista[(i+1)]:
        	resultado=resultado+1
        if lista[i] != lista[(i+1)]:
        	resultado=resultado+0
        i=i+1
    return resultado