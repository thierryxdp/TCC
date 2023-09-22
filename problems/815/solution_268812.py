def insere(lista_numero,n):
    '''funçao que dada uma lista ordenada crescente de numeros inteiros e 
    um numero n, inclua na posiçao correta, de tal maneira q a lista
    continue ordenada'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero