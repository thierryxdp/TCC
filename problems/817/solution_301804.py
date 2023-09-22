def maiores (lista,n):
    """Função que dada uma lista de número inteiros e um novo número inteiro, retornara uma nova lista em ordem crescente apenas com os elementos que forem maiores que n.
    casos de teste:
    entrada:([1,2,3,4,5,6,7],4) saida:[5,6,7]
    entrada:([2,4,6,8],3) saida:[4,6,8]
    entrada:([1,3,5,7,9],2) saida:[3,5,7,9]
    assinatura: list, int -> list"""
    nova_lista = []
    for e in lista:
        if e > n:
            list.append(nova_lista,e)
            list.sort(nova_lista)
    return nova_lista

def acima_da_media(lista):
    for e in lista:
        a = sum(lista) / len(lista)
    return maiores(lista,a)