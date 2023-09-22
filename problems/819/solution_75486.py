def filtraMultiplos(numeros: list, n: int) -> list:
    """Função filtra os números da lista para aqueles que são divisíveis 
       de n

       Parameters:
       numeros: lista de números
       n: número

       Return:
       lista com os números da lista que forem divisíveis por n
    """

    divisiveis = []
    i = 0

    while i < len(numeros):
        if numeros[i]%n == 0:
            divisiveis += numeros[i]
        i = i + 1
    return divisiveis