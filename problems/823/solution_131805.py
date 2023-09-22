def faltante(lista):
    """Função que nos retorna a peça que está faltando no quebra-cabeça de Little John.
    list -> int """

    n = 1

    while n <= len(lista) - 2:
        if lista[n+1] - lista[n] != 1:
            faltante = ((lista[n] + lista[n-1])/2)
            lista.append(faltante)

        n = n + 1

    
    if lista[0] != 1:
        return 1


    elif lista[-1] == n + 1:
        return n + 1

    else:
        return int(faltante)