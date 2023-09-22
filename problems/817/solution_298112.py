def acima_da_media(lista):
    """Retorna apenas as notas dos alunos acima da media;
    	list -> list"""
    n = sum(lista)/len(lista)
    if n in lista:
        list.sort(lista)
    	x = list.index(lista,n)
    	return lista[x+1:]
    elif len(lista) == 1:
        return []
    else:
    	list.insert(lista,0,n)
    	list.sort(lista)
    	x = list.index(lista,n)
    	return lista[x+1:]