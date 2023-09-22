def repetidos(lista):

    #Receba como entrada uma lista de números, e retorne o número de vezes que um elemento da lista é igual ao elemento anterior; Lista(int) => int#

    qtd_repetidos = 0


    for i in range(1, len(lista)):

        if(lista[i-1] == lista[i]):

            qtd_repetidos += 1


    return qtd_repetidos