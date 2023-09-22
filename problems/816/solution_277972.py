def maiores (lista_inteiros, n):
    """klmgkdg"""
    
    if sorted(lista_inteiros)[-1] < n:
        return ()
    else:
        maior = n for n in lista_inteiros if lista_inteiros > n
        return maior