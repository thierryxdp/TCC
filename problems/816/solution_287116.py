def maiores(lista,n):
    '''função que recebe uma lista e um número inteiro n e retorna
    uma lista que contenha todos os números da lista original maiores
    que n e em ordem crescente
    list,int->list'''
    
    list(lista)
    lista.append(n)
    lista_ordenada=sorted(lista)
    indice_n=lista_ordenada.index(n)
    
    if n not in lista_ordenada:
        lista.append(n)
    
    return lista_ordenada[indice_n+1:]