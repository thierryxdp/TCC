def maiores (lista_inteiros, n):
    """klmgkdg"""
    lista_n = [n]
    if max(lista_inteiros) < n:
        return []
    
    else:
        maior = [n for n in lista_inteiros if lista_inteiros > lista_n]
        return sorted(maior)