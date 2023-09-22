def filtraMultiplos(lista,n):
    """A função filtra a lista retornando apenas os múltiplos
	de n; list,int->list"""
    lista_multiplos=[termo for termo in lista if termo %n==0]
    multiplos=lista_multiplos
    return multiplos