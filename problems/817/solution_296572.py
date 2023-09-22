def acima_da_media(lista):
    '''função que calcula a média de notas de uma turma e retorna as notas a cima da média
    lista[] -> Lista[]'''
    def maiores(lista, n):
    	'''função que insere um número na lista e retorna os elementos maiores que ele de forma ordenada
    	Lista[],Int -> Lista[]'''
    	list.append(lista,n)
    
    	list.sort(lista)
    
    	return lista[list.index(lista,n)+1:]

	media = sum(lista)/len(lista)
    
    return list.remove(maiores(lista, media), media)