def lingua_p(palavra):
    """str --> str """
    lista = list(palavra)
    traducao = ''
    for i in lista:
        if i in 'aeiouáéíóú':
            traducao += i + 'p' + i
        else:
            traducao += i
    return traducao