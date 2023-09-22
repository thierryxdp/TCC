def maiores(lista, n):
    
    """Funçao que recebe uma lista de numeros inteiros e um numero inteiro 'n' e retorna outra lista
    que contenha todos os numeros da lista original maiores que 'n'"""
    
    list.append(lista,n)
    list.sort(lista)
    x = list.index(lista,n)
    
    return lista[x+1:]