def insere(lista_numero,n):
    """Função adiciona o número no fim da lista e ordena crescentemente.
    lista, int-> lista"""
    lista_numero+=[n]
    lista_numero.sort()
    return lista_numero