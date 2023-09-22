def acima_da_media(lista_inteiros, n):
    #Essa função dada uma lista de numeros inteiros, um numero inteiro n
    #retorna uma lista com todos os numeros da lista original maiores que n
    list.insert(lista_inteiros,0,n)
    list.sort(lista_inteiros, reverse=true)
    x = list.index(lista_inteiros,n,0)
    del lista_inteiros[x::]
    return lista_inteiros[::-1]