def insere(lista_numero:list, n:int) ->list:
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero