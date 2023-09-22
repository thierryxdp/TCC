def insere(lista_numero, n):
    """Recebe uma lista numérica ordenada e um valor inteiro, e retorna uma nova lista com 
    os valores ordenados na ordem crescente
    assinatura: lista, int --> lista
    testes:
    insere([1, 3, 4, 5], 2)==[1, 2, 3, 4, 5]
    insere([2, 5, 6], 1)==[1, 2, 5, 6]
    """
    lista=list.append(lista_numero, n)
    lista=list.sort(lista) 
    return lista