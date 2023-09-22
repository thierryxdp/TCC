def insere(lista,n):
    """essa função dada uma lista ordenada (crescente) de números inteiros (igual ao
parâmetro de entrada lista) e um número inteiro n, inclui n na posição correta, ou
seja, de tal maneira que a lista continue ordenada.
list,int -> list"""
    list.append(lista,n)
    list.sort(lista)
    return lista

def maiores(lista,n):
    """essa função dada uma lista de números inteiros(igual ao parâmetro de entrada
lista) e um número inteiro n, retorna outra lista, que contém todos os números da
lista original maiores que n ordenados em
ordem crescente.
list,int -> list"""
    if n in lista:
        list.sort(lista)
        indice=list.index(lista,n)
        return lista[indice+1:]
    else:
        insere(lista,n)
        indice=list.index(lista,n)
        return lista[indice + 1:]