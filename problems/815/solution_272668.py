def insere(lista_numero,n):
    '''retorna a lista na ordem crescente com o numero n incluso'''
    lista_numero.extend(n)
    return sort(lista_numero)