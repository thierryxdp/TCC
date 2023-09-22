def repetidos (numeros: list)-> int:
    """Função que dado um número, calcula e retorna o fatorial desse."""
    fatorial = 1
    i = 1
    while i <= len(numeros):
        fatorial = fatorial*i
        i = i + 1
    return fatorial