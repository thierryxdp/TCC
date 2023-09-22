def maiores(lista,n):
    '''funçao que recebe uma lista de numeros inteiros e um numero inteiro n e retorna outra 
    lista contendo todos os numeros da lista original maiores que n, ordenados em ordem crescente
    lista,int-->list'''
    lista2=[]
    i=0
    while i<len(lista):
        if lista[i] > n:
            lista2=lista2+[lista[i],]
            list.sort(lista2)
            return lista2