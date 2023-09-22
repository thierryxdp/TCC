def insere(lista_numero,n):
    '''Função que retorna um número n na posição correta de tal
    maneira que a lista crescente continue ordenada.
    lista_numero=list,n=int->list'''
    x = list.append(lista_numero,n)
    y = list.sort(lista_numero)
    return y