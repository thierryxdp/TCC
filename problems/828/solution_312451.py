def primo (n):
    """Recebe um número inteiro positivo, e retorna um valor
    booleano indicando se é primo ou não.
    int -> bool"""
    divisores = []
    indice = 1
    while i < n+1 and len(divisores) > 2:
        if n % indice == 0:
            list.append (divisores, indice)
        indice += 1
    if divisores[1] == n:
        return True
    else:
        return False