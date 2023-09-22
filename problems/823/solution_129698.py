def faltante(lista_pecas:list)->int:

    """ Função que, dada uma lista com N -1 inteiros merados de 1 a N, descubra
        qual núumero inteiro deste intervalo está faltando

    """

    n = 0
    list.sort(lista_pecas)
    verificador = list(range(1,(len(lista_pecas)+2)))

    if lista_pecas[len(lista_pecas)-1] != verificador[len(verificador)-1]:

        return verificador[len(verificador)-1]

    else:

        while lista_pecas[n] == verificador[n]:

            n += 1

        return verificador[n]