def repetidos(listaNum):
    '''Recebe uma lista de números e retorna o número de vezes que um
    elemento da lista é igual ao elemento anterior

    list -> int'''

    indice = 1
    num_igual_ant = 0

    while indica < len(listaNum):
        if listaNum[indice] == listaNum[indice-1]:
            num_igual_ant = num_igual_ant + 1
        
        indice = indice + 1

    return num_igual_ant