def insere(lista_num,n):
    '''funçao que dada uma lista ordenada(crescente) de numeros 
    inteiros e um numero inteiro n, inclui n na posiçao correta na lista.
    list,int -> list'''
    lista_num.append(n)
    lista_num.sort()
    return lista_num

def acima_da_media(numeros,numero):
    '''funçao que dada uma lista de numeros inteiros e um numero inteiro n,
retorna outra lista, que contenha  todos os numeros da lista original maiores
que n, ordenados em ordem crescente.
list,int -> list'''
    crescente =insere(numeros,numero)
    posicao = crescente.index(numero)
    del crescente[0:posicao+1]
    return crescente