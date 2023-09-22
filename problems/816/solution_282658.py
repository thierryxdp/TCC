def maiores(numeros, n):
    '''funcao que, dada uma lista de numeros inteiros e um numero n de entrada, retorna
    uma nova lista que contem apenas os numeros maiores que n, os quais estarao ordenados
    de maneira crescente;
    list(int),int->list(int)'''
    lista=numeros+[n]
    list.sort(lista)
    indice_n=list.index(lista,n)
    return lista[indice_n+1:]