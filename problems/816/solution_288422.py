def maiores(inteiros,n):
    '''função resposável por adicionar um termo, n, a lista, inteiros, e retornar uma lista que apresente os números da lista inteiros que são maiores que o termo n'''
    list.append(inteiros,n)
    list.sort(inteiros)
    posto=list.index(inteiros,n)
    return inteiros[posto+1:]