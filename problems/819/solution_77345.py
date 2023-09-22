def filtraMultiplos(lista,n):
    """retorna uma lista com os elementos divisíveis por n
	list,int-> list"""
    
    lista1=[]
    for i in lista:
        if i//n == 0:
            lista1.append(i)
    return lista1