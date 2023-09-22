def lingua_p(frase):
    """função que recebe uma frase e traduz ela para a lingua do p..
    str -> <acumulador> """
    acumulador = ''
    for i in range(len(frase)):
        if frase[i] in 'aeiouáéíóú':
            acumulador = acumulador+frase[i] + 'p' + frase[i]
        else:
           acumulador = acumulador + frase[i]
    return acumulador