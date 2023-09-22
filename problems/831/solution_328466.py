def lingua_p(frase):
    """função que recebe uma frase e traduz ela para a lingua do p.
    Na linguagem do p após cada vogal da palavra original é inserida
    a sequência de letras 'p' mais a vogal original.
    str -> <acumulador> """
    acumulador = ''
    for i in range(len(frase)):
        if frase[i] in 'aeiou':
            acumulador = acumulador+frase[i] + 'p' + frase[i]
        else:
           acumulador = acumulador + frase[i]
    return acumulador