def multiplos(list_de_num, n):

    '''Determina os mútiplos de n na lista de números dada '''

    # list, int -> list

    resposta = []

    for num in list_de_num[0:]:

        if num % n == 0:

            resposta.append(num)

    return resposta