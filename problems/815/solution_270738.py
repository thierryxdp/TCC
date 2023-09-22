def insere(lista_numero,n):
    '''funcao que dada uma lista ordenada e 
    um numero n calcule se a lista continua ordenada'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero