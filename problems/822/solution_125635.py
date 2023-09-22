def repetidos(numeros):
    '''uma funç~so chamada repetidos que recebe 
    como entrada uma lista de numeros, e retorne o numero
    de vezes que um elemento da lista ́e igual ao elemento 
    anterior. list[int] ->int'''
    i=0
    cont=0
    while i<len(numeros):
        if numeros[i-1] == numeros[i] :
            cont=cont+1
        i=i+1
    return cont