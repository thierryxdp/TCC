def insere(lista_numero,n):
    '''Dada uma lista de números e um número 'n', será inserido 'n' na posição
    correta de modo crescente.(lista,int=>lista)'''

    lista_numero = lista_numero + [n]
    list.sort(lista_numero)

    return lista_numero