def insere(lista_numero, n):
    '''funcao pega um numero fora da lista e o insere dentro e de modo que fique na ordem'''
    lista_numero.append(n)
    lista_numero = sorted(lista_numero)
    return(lista_numero)