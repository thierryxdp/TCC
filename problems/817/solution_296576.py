def maiores(listanumeros,n):
    """
    Função recebe uma lista de números inteiros(listanumeros) e um números inteiro n,
    retorna outra lista que contenha todos os números da lista original maiores do que n,
    ordenados em ordem crescente.
    lista, int -> lista
    """
    list.append(listanumeros,n)
    list.sort(listanumeros)
    vezes=list.count(listanumeros,n)
    posicao=list.index(listanumeros,n)+vezes-1
    return listanumeros[posicao:]
def acima_da_media(notas):
    """
    
    """
    media=sum(notas)/len(notas)
    return maiores(notas,media)