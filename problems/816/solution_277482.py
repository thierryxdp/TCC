def maiores(lista, n):
    """Função que, dada uma lista de números inteiros e um número n, retorna outra lista, com todos os números da lista original maiores que n
    entrada: list, n
    saída: list"""
    
    a = list.sort(lista)
    b = list.append(lista, n)
    
    
    return b