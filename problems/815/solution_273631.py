def insere(lista_numero, n):
    '''Função que dado uma lista crescente de numeros inteiros e um número inteiro n,
    inclua esse numero na posição certa, de maneira que a lista permaneça ordenada.
    lista_numero -> list
    n -> int
    return -> list'''
    
    lista = lista_numero 
    
    lista.append(n)
    lista.sort()
    
    return lista