def insere(lista_numero,n):
    """Função q insere número em uma lista e retorna em ordem crescente"""
    """List -> List"""
    lista = lista_numero.append(n)
    lista = lista.sort()
    return lista