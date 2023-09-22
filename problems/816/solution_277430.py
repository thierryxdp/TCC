def maiores(lista_numeros,n):
    "função que dada uma lista de números inteiros e um número 'n' retorna uma nova lista com todos os números da lista original maiores que 'n'.list->list."
    lista_numeros.append(n+1)
    lista_numeros.sort()
    posicao = lista_numeros.index(n+1)
    return lista_numeros[posicao+1:]