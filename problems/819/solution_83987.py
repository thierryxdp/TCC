def filtraMultiplos(lista,n):
    """Funcao que verifica os elementos da lista divisiveis
    por n. list,int->list"""
	proximo = 0
    l = []
    while lista[proximo]%n==0:
    	list.append(l,lista[proximo])
    proximo = proximo + 1
    return l