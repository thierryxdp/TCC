def acima_da_media(lista):
    def maiores(lista, n):
    	'''função que insere um número na lista e retorna os elementos maiores que ele de forma ordenada
    	Lista[],Int -> Lista[]'''
    	list.append(lista,n)
    
    	list.sort(lista)
    
    	return lista[list.index(lista,n)+1:]

    media = round(sum(lista)/len(lista),0)
    
    return maiores(lista,media)