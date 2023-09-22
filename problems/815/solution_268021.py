def insere(lista_de_numeros,n):
    """Esta é a função que dado um número e uma lista ordenada de números inteiros ordena os números em ordem crescente e adiciona o número n na posição correta, list, int -> lis"""
    lista1 = lista_de_numeros + [n]
    lista_ordenada = list.sort(lista1)
    return lista_ordenada