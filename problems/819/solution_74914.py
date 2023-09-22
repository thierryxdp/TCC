def filtraMultiplos(lista,numero):
    """Retorna uma lista contendo os elementos da lista original divisiveis por numero.list,int-->list"""
    i=0
    divisiveis=[]
    while i<=len(lista):
        if lista[i]%numero==0:
            divisiveis=divisiveis+[lista[i]]
        i=i+1
	return divisiveis