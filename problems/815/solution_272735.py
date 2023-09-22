def insere(lista_numero, n):
    """Essa funçaõ acrescenta um número inteiro e mantém a lista de forma ordenada."""
    lista_numero.insert(0, n)
    return sorted(lista_numero)