def insere(lista_numero,n):
    """FUnção que calcula uma lista dade e adiciona um novo elemento a lista dado de entrada e retorna uma lista com o numeor adicionado e em ordem crescente
    list, int -> list"""
    listadd = lista_numero + [n]
    list.sort(listadd)
    return listadd