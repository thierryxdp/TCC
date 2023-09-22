# str,int->list
def maiores(lista,n):
    "Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n."
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)
    lista=lista[:posicao:-1]
    list.reverse(lista)
    return lista