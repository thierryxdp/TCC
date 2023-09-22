def insere(lista_numero,n):
    """dado a lista de numeros, transformamoss n em uma lista para atribui-lo
    em nossa lista antiga, depois colocamos a nova lista na ordem crescente
    list, int -> list"""
    n=[n]
    lista=lista_numero+n
    lista.sort()
    return lista