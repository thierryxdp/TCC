def primo(n):
    """Dado um numero inteiro positivo n, retorna se ele é primo (True)
    ou nao (False)
    int -> bool"""
    lista = list(range(1,n))
    lista_impares = lista[2::2]
    if n%2 == 0:
        return False
    for s in lista_impares:
        if n%s == 0:
            return False
    return True