def faltante(lista):
    'retorna um elemento que completa uma lista; list->int'
    f=1
    lista.sort()
    while f<len(lista):
        if lista[f]- lista[f-1]>1:
            return lista[f]-1
        f=f+1
    if 1 in lista:
        return len(lista)+1
    else:
        return 1