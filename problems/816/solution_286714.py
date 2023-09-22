def maiores(ls,n):
    '''Função que, dada uma lista de números inteiros e um 
    número n, retorna outra lista, contendo apenas os números 
    da lista original maiores que n, em ordem crescente.
    assinatura: list, int -> list '''
    list.append(ls,n)
    list.sort(ls)
    posicao = list.index(ls,n) 
       
    return ls[posicao+1:]