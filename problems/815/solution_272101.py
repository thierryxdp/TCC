def  insere ( lista_numero , n ):
    """ funcao que dada uma lista ordenada crescente, e um numero inteiro n,
    inclui esse numero na lista de maneira ordenada """
    lista_numero.insert(0,n)
    list.sort(lista_numero)
    return lista_numero