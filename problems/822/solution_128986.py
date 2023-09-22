def repetidos(lista):
        qtd_repetidos = 0

    for i in range(1, len(lista)):

        if(lista[i-1] == lista[i]):

            qtd_repetidos += 1

    return qtd_repetidos