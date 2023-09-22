def faltante(lista):
    """ Para retornar o número que está faltando na sequencia, digite;
    list->list"""
    list.reverse(lista)
    n=lista[0]
    list.sort(lista)
    i=0
    x=0
    while i<n:
        x += 1
        if x != lista[i]:
            return x
        i += 1
    return i+1