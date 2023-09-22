def primo(n):
    """retorna se o número é primo ou não"""
    lista = list(range(1,n))
    i = 0
    div = 0
    while i < len(lista):
        if n % lista[i] == 0:
            div = div + 1
        i = i + 1
        
    if div < 2:
        return True
    else:
        return False