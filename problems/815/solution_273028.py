def insere(lista_numero,n):
    '''Dada uma lista de números e um número 'n', será inserido 'n' na posição
    correta de modo crescente'''

    lista_numero = lista_numero + [n]
    lista_numero = list.sort(lista_numero)

    return lista_numero