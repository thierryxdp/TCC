def maiores(lista,n):
    """funcao que dado uma lista e um numero inteiro retorna outra lista com todos os numeros inteiros maiores que n"""
	"""list,int->list"""
    
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    ind = list.index(lista,n)
    listaf = lista[ind+1:]
    return listaf

def acima_da_media(lista):
    """funcao que dada uma lista de notas retorna uma lista ordenada com as notas que ficaram acima da media"""
	"""list->lista"""
    
    media = sum(lista)/len(lista)
    
    return maiores(lista,media)