def acima_da_media(lista:list) ->list:
    """Recebe uma lista com notas de alunos e retorna outra lista com apenas
    	as notas acima da média dos valores da lista"""
    n = sum(lista)/len(lista)
    list.append(lista, n)
    list.sort(lista)
    
    if list.count(lista, n) == 2:
        return lista[list.index(lista,n)+2:]
    
    else:
    	return lista[list.index(lista,n)+1:]