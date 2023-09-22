def insere(lista_numero:list,n:int)->list:

    """ Função que recebe uma lista e um número inteiro n e retorna o número n
        em uma nova lista ordenada numa posição tal qual
        não desordene a ordem crescente da lista original.

    """

    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero