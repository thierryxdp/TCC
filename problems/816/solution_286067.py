def maiores(lista_inteiros,n):
    """dada uma lista de numeros inteiros e um numero n, retorna uma lista
    que contenha todos os numeros da lista original maiores que n"""
    
    lista_inteiros.append(n)
    
    lista_inteiros.sort()
    
    return lista_inteiros[0:n]