def filtraMultiplos(lista,num):
    '''
		Função que recebe uma lista e um número e resulta em uma lista com todos
        os valores multiplos daquela lista refente aquele número.
        list, int -> list
    '''
    i=0
    result=[]
    while (i < len(lista)):
    	if (lista[i]%num == 0):
            divisivel = lista[i]
    		result.append(divisivel)
    	i+=1
    return result