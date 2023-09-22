def maiores (lista_inteiros,n):
    """função que dada uma lista de números inteiros
    'lista_inteiros' e um número inteiro 'n', retorna outra 
    lista, que contenha todos os números da lista original 
    maiores que n, ordenados em ordem crescente"""
    list.append(lista_inteiros,n)
    list.sort(lista_inteiros)
    indice_n= list.index(lista_inteiros,n)
    return lista_inteiros[indice_n+1:]