def maiores(lista,n):
    '''funcao que retorna uma nova lista de forma crescente, contendo
    da lista original apenas os numeros inteiros inseridos na lista (posicao 0)
    que são maiores que n (posicao1)
    list,int->list'''
    lista[:]=lista
    lista= lista[:]+[n]
    posicao=list.sort(lista)
    ident= list.index(lista,n)
    funcao= lista[ident+1:]
    return funcao