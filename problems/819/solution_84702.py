def filtraMultiplos(lista,n):
    '''Função que recebe uma lista e um número n e retorna outra lista contendo os múltiplos de n que estão na lista original;
list,float->list'''
	i=0
	multiplos=[]
	while i<len(lista):
        if lista[i]%n==0:
            list.append(multiplos,lista[i])
    	i=i+1
    return multiplos