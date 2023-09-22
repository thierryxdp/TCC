def maiores(lista_numerica, n):
    '''
        recebe uma lista numerica e um numero inteiro retornando uma lista
        ordenad em ordem crescente, comosta pelos numeros maiore que o numero
        recebido
        entrada: lista, interiro
        saida: lista
    '''
    list.append(lista_numerica, n)
    list.sort(lista_numerica)
    list.reverse(lista_numerica)
    p=list.index(lista_numerica, n)
    lista_numerica=lista_numerica[0:p]
    list.reverse(lista_numerica)
    return lista_numerica