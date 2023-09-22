def insere(lista_numero,n):
    '''Função que dada uma lista ordenada crescente retorna os números na posição correta
    list,int->list'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero