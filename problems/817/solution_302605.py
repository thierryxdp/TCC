def acima_da_media(lista):

    '''função que dada uma lista com as notas dos alunos retorna aquelas acima da média;

    list->list'''

    n = sum(lista)/len(lista)

    list.append (lista,n)

    list.sort(lista)

    a = list.index(lista,n)

    indice = a+1

    if lista[a+1] > n:

    	return lista[indice:]    else:

          return []