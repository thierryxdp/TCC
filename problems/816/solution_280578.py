def maiores(lista,n):
    """Função que, dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n,
    lista --> lista"""
    
    if n not in lista:
        list.append(lista,n)
       
    list.sort(lista)
    indice = list.index(lista,n)
    
    fatiado = lista[indice + 1:]
    
    return fatiado