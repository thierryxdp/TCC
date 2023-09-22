def insere(lista,n):
    """Esta funcao recebe uma lista e um numero, adiciona esse numero na lista de forma que ela continue crescente
    str -> str"""
    lista.insert(0,n)
    lista.sort()
    return lista