def insere(lista_numero,n):
    '''Função que dada uma lista numerada em ordem crescente e um número intero n, retorna uma lista com a o número inteiro incluso e em ordem crescente'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero