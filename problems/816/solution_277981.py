def maiores (lista_inteiros, n):
    """klmgkdg"""
    lista_n = [n]
    if sorted(lista_inteiros)[-1] < n:
        return []
    elif sorted(lista_inteiros)[0] < n:
    else:
        maior = [n for n in lista_inteiros if lista_inteiros > lista_n]
        return sorted(maior)