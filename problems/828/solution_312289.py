def primo(n):
    """Dado um numero inteiro positivo n, retorna se ele é primo (True)
    ou nao (False)
    int -> bool"""
    lista = list(range(2,n))
    lista_impares = lista[::2]
    for s in lista_impares:
        if n%s == 0:
            return False