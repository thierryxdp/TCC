def insere(lista_numero,n):
    '''A funcao recebe uma lista de numeros e um numero n e retorna a lista com o n
incluso na posicao certa de ordem crescente list,int->list'''
    lista=lista_numero.append(n)
    return lista.sort()