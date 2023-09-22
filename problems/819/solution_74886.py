def filtraMultiplos(listagem:list,n:int)->list:

    """ Função que a recebe de entrada uma lista de números e um número n e retorna
        somente os números da lista que são divisíveis por n.

    """

    cont = 0
    nova_lista = []

    while cont<len(listagem):

        if listagem[cont]%n == 0:

            nova_lista = nova_lista + listagem[cont]

        cont += 1

    return nova_lista