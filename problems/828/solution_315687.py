def qtd_divisores(n):
    qtd = 0
    for numero in range(1, n+1):
        if n%numero == 0:
            qtd +=1
    return qtd
def primo(n):
    """Retorna um booleano que garante se um número inteiro
    positivo dado como entrada é número primo ou não.
    int -> bool"""
    if qtd_divisores(n) > 2:
        return False
    else:
        return True