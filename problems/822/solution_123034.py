def repetidos(lista):
    ''funcao que recebe uma lista de numeros e retorna o numero de vezes que um elemento da lista e igual ao elemento anterior''
    i = 1
    j = 0
    cont = 0
    while (i < len(lista)):
        if (lista[i] == lista [j]):
            cont  += 1
            i += 1
            j +=  1
        else:
            i += 1
            j += 1
    return cont