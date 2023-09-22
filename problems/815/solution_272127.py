def insere(lista_numero,n):
    """dada uma lista e um numero inteiro, inclui o numero na lista;
    list,int->list."""
    d=[n]
    lista=lista_numero
    teste=list.extend(lista,d)
    teste=list.sort(teste)
    return teste