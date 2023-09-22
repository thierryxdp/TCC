def repetidos(lista):
    """
    lista->int
    :param lista: Recebe lista de números
    :param return: Retorna a quantidade de vezes que o numero da lista é igual
    o anterior.
    """
    i = 1
    count = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            count += 1
        i = i + 1
    return count