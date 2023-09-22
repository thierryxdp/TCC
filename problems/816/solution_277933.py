def maiores(lista_inteiros,n):
    #Essa função dada uma lisa de numeros inteiros e um numero inteiro n
    #Retorna uma outra lista que contenha todos os numeros da lista original maiores que n
    list.insert(lista_inteiros,0,n)
    list.sort(lista_inteiros,reverse=True)
    x = list.index(lista_inteiros,n,0)
    del lista_inteiros[x::]
    
    return lista_inteiros[::-1]