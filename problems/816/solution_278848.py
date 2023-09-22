def maiores(lista,n):
    """Recebe uma lista de números inteiros e um número inteiro n e retorna uma lista
       com todos os números da lista original que são maiores que o número n.
       list, int->list

       Parameters:
       lista: Uma lista de números inteiros.
       n: Um número inteiro."""
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)+1
    return lista[posicao:]