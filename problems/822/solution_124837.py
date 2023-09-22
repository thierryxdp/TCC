def repetidos(lista):
    i_inicial=0
    i_posterior= i_inicial+1
    repeticoes=0
    while i_posterior<len(lista):
        if lista[i_posterior]==lista[i_inicial]:
            repeticoes=repeticoes+1
            inicial=inicial+1
        elif lista[i_posterior]!=lista[i_inicial]:
            inicial=inicial+1
            repeticoes=repeticoes
    return repeticoes