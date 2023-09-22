def maiores(lista, n):
    """Função que, dada uma lista de números inteiros e um número inteiro n, retorna outra lista com todos os números da lista original que são maiores que n
    entrada: list, int
    saída: list"""
    
    list.append(lista, n)
    list.sort(lista)
    indice = list.index(lista, n)
    lista_nova = lista[indice+1:]
    
    return lista_nova