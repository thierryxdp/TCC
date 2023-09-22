def maiores(lista_numeros, n):
    '''Função que recebe uma lista de números inteiros e um número inteiro n, retorna outra lista contendo
    os números da lista original que são maiores que n.
    list, int - > list'''
    
    if n in lista_numeros:
        list.remove(lista_numeros, n)
    
    
    list.append(lista_numeros, n)
    list.sort(lista_numeros)
    
    indice = list.index(lista_numeros, n)
    
    return lista_numeros[indice+1:]