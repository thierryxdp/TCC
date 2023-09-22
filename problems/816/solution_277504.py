def maiores(lista,n):
    """dada uma lista de números inteiros e um número inteiro n, a
função retorna outras lista contendo todos os números da lista original
maiores que n.
list,int-->list

Parâmetros
lista: lista de inteiros inicial utilizada como entrada
n: número inteiro"""
    y=list.append(lista,n)
    x=list.sort(lista)
    return lista[list.index(lista,n)+1:]