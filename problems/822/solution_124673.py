def repetidos(lista):
	'''Função que recebe uma lista e retorna o numero de vezes que um elemento da lista é igual ao anterior'''
	'''list->int'''
    i=1
    r=[]
    while i < len(lista):
        if lista[i]==lista[i-1]:
            r.append(lista[i])
        i=i+1
    return len(r)