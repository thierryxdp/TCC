def intercala(lista1, lista2):
    """retorna a lista1 intercalada com a lista2;
    	list,list->list"""
    listavf= list(lista1[0])+list(lista2[0])+list(lista1[1])+list(lista2[1])+list(lista1[2])+list(lista2[2])
    return listavf