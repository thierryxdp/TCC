def insere(lista_num,n):
    '''funçao que dada uma lista ordenada(crescente) de numeros 
    inteiros e um numero inteiro n, inclui n na posiçao correta na lista.
    list,int -> list'''
    lista_num.append(n)
    lista_num.sort()
    return lista_num

def maiores(numeros,numero):
    '''funçao que dada uma lista de numeros inteiros e um numero inteiro n,
retorna outra lista, que contenha  todos os numeros da lista original maiores
que n, ordenados em ordem crescente.
list,int -> list'''
    crescente =insere(numeros,numero)
    posicao = crescente.index(numero)
    del crescente[0:posicao+1]
    return crescente

def maiores2(numeros,numero):
    '''funçao que dada uma lista de numeros inteiros e um numero inteiro n,
retorna outra lista, que contenha  todos os numeros da lista original maiores
que n, ordenados em ordem crescente.
list,int -> list'''
    crescente =insere(numeros,numero)
    posicao = crescente.index(numero)
    del crescente[0:posicao+2]
    return crescente

def acima_da_media(notas):
    quant_notas=len(notas)
    media=sum(notas)/quant_notas
    if len(notas)=1:
        return maiores2(notas,media)
    else:
        return maiores(notas,media)