def repetidos(lista):
    """Retorna o numero de vezes que um elemento da lista e igual ao anterior.list-->int"""
    i=0
    vezes=0
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            vezes=vezes+1
        else:
            vezes= vezes+0
        i=i+1
	return vezes