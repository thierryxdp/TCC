def insere(lista_numero,n):
    """dada uma lista crescente e um int n, a funçao retorna n
    na sua posiçao ordenada
    list,list->list"""
    l = lista_numero
    list.extend(lista_numero, [n])
    l.sort()
    return l