def maiores(lista,n):
    """funcao que dada uma lista de numeros inteiros e um numero inteiro n, retorna
    outra lista, que contem todos os numeros da lista original maiores que n, 
    em ordem crescente
    list,int->list"""
    lista2 = []
    i = 0
    while i<len(lista):
        if lista[i] > n:
            lista2 = lista2 +[lista[i],]
            lista3 = list.sort(lista3)
        i=i+1
    return lista2