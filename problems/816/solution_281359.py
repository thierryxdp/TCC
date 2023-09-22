def maiores(lista_numero,n):
    '''
       função que recebe uma lista de numeros inteiros e
       um numero inteiro n, e retorna outra lista, que 
       contenha todos os numeros da lista original maiores
       que n 
       list,int -> list
    '''
    lista_numero.append(n)
    lista_numero.sort()
    posicao = lista_numero.index(n)
    return lista_numero[posicao+1:]