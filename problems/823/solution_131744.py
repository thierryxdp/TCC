def faltante(lista):
    """Função que nos retorna a peça que está faltando no quebra-cabeça de Little John.
    list -> int """

    n = 0
    lista_ordenada = sorted(lista)

    while n <= len(lista_ordenada) - 1:
        if lista_ordenada[n] - lista_ordenada[n-1] != 1:
            faltante = ((lista_ordenada[n] + lista_ordenada[n-1])/2)

        else:
            faltante = lista_ordenada[n] + 1


    return int(faltante)