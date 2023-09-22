def maiores(lista,n):
    '''funcao que retorna uma nova lista de forma crescente, contendo
    da lista original apenas os numeros inteiros inseridos na lista (posicao 0)
    que são maiores que n (posicao1)
    list,int->list'''
    lista[:]=lista
    x=list.sort(lista)
    
    lista2= lista[:]+[n]
    y=list.sort(lista2)
    ident= list.index(lista2,n)
    
    if lista>[n]:
        return lista
    else:
        return lista2[ident+1:]