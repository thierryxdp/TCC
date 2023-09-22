def insere(lista_numero,n):
    '''funcao que dada uma lista ordenada e 
    um numero n calcule se a lista continua ordenada'''
    list.sort(lista_numero)
    lista_numero.append(n)
    return lista_numero