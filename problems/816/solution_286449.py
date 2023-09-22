def maiores(x,n):
    'Função que dada uma lista de números inteiros e um número inteiro n, retorna uma lista apenas com os números inteiros maiores que n da lista original'
    'list, int->list'
    list.append(x,n)
    list.sort(x)
    z=len(x)
    y=list.index(x,n)
    return x[y+1:z]