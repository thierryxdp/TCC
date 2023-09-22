def filtraMultiplos (lista_numeros: list, n: int) -> list:
    """Recebe uma lista de numeros e um numero n, retorna uma lista com 
    todos os números em lista_numeros que são divisíveis por n."""
    lista_com_divisiveis = []
    tamanho_lista = len(lista_numeros)
    contador = 0
    while contador < tamanho_lista:
        if lista_numeros[contador] % n == 0:
            lista_com_divisiveis.append(lista_numeros[contador])
        contador += 1
    return lista_com_divisiveis