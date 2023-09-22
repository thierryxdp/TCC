def maiores(lista_numero,n):
    """Função que dada uma lista de números inteiros e um número inteiro n,
retorna outra lista com todos os números da lista original maiores que n em
ordem crescente; list,int -> list"""
    lista=lista_numero+[n]
    list.sort(lista)
    indice=lista.index(n)
    return lista[indice+1:]