def faltante(lista):
    """Função que nos retorna a peça que está faltando no quebra-cabeça de Little John.
    list -> int """

    n = 0
    lista_ordenada = sorted(lista)

    while n <= len(lista_ordenada) - 1:
        if lista[n] - lista[n-1] != 1:
            faltante = ((lista[n] + lista[n-1])/2)
        n = n + 1

    return int(faltante)