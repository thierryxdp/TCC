def insere(lista_numero:list, n:int) ->list:
    """Recebe uma lista de números em ordem crescente e um número, e retorna 
    uma nova lista com esse número inserido, sem quebrar a forma crescente da lista"""
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero