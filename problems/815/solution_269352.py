def insere(lista_numero , n):
    """Função que ordena uma lista incluindo um numero inteiro n. List-->List"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero