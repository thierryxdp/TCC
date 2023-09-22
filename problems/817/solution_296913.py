def acima_da_media(lista):
    '''Função que calcula a média de notas de uma turma, e retorna uma lista de notas a cima da média
    Lista[] -> Lista[]'''
    
    def maiores(lista, n):
    	'''função que insere um número na lista e retorna os elementos maiores que ele de forma ordenada
    	Lista[],Int -> Lista[]'''
    	list.append(lista,n)
    
    	list.sort(lista)
    
    	return lista[list.index(lista,n)+1:]

    media = sum(lista)/len(lista)
    
    #impedir que a média seja colocada na lista de retorno
    if(media in lista):
        nova = maiores(lista,media)
        return nova[1:]
    else:
    	return maiores(lista,media)