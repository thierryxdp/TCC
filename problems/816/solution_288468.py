def maiores(lista,n):
    '''funçao que recebe um alista de numeros inteiros e um numero inteiro n e retorna outra
    lista que contem todos os numeros da lista original maiores que n, ordenados em ordem crescente
    int,list-->list'''
    lista2=[]
    i=0
    while i<len(lista):
        if lista [i] > n:
            lista2 = lista2 + [lista[i]]
            list.sort(lista2)	
    	i=i+1
    return lista2