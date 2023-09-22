def filtra_pares(tupla_inicial):
    '''
    Funcao que gera uma nova tupla a partir da tupla original de quatro numeros recebida,
    assim filtrando os elementos pares da original e cria a nova tupla contendo somente esses pares
    
    tupla_inicial = inserir 4 elementos inteiros da seguinte maneira ([el_1, el_2, el_3, el_4])
    tuple -> tuple
    '''

    el_1, el_2, el_3, el_4 = tupla_inicial 
    tupla_pares = tuple()

    if el_1 % 2 == 0:
        tupla_pares += (el_1, )

    elif el_2 % 2 == 0:
        tupla_pares += (el_2, )

    elif el_3 % 2 == 0:
        tupla_pares += (el_3, )

    elif el_4 % 2 == 0:
        tupla_pares += (el_4, )

    return tupla_pares