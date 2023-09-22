def faltante(lista):
    """Função que nos retorna a peça que está faltando no quebra-cabeça de Little John.
    list -> int """

    n = 1

    while n - 1<= len(lista) - 2:
        if lista[n] - lista[n-1] != 1:
            faltante = ((lista[n] + lista[n-1])/2)
        n = n + 1

    
    if lista[0] != 1:
        return 1


    elif int(faltante) not in lista:
        return int(faltante)

    else:
        return n + 2