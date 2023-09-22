def filtros(lista,n):
    #A primeira resposta que eu mandei foi um teste, por favor
    #considere issa resposta 
	'''Dada uma lista, e o número de n. Retorna o filtragem dos
elementos da lista que são múltiplos de n'''
    proximo=0
    multiplos=[]
    while proximo<len(lista):
        if lista[proximo]%n==0:
            list.append(multiplos,lista[proximo],)
        proximo=proximo+1
    return multiplos