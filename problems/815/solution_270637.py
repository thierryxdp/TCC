def insere(lista_numero, n):
    """função que dada uma lista ordenada e um número inteiro 'n', retorne a lista com o número inserido na ordem correta; list, int -->list"""
    lista_numero= lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero