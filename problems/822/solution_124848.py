def repetidos(lista):
    '''função que retorna a quantidade de vezes que um numero
    dentro da lista parece consecutivamente
    lista-> int'''
    i_inicial=0
    i_posterior=1
    repeticoes=0
    while i_posterior<len(lista):
        if lista[i_inicial]==lista[i_posterior]:
            repeticoes=repeticoes+1
            i_inicial=i_inicial+1
            i_posterior=i_posterior+1
        elif lista[i_posterior]!=lista[i_inicial]:
            i_inicial=i_inicial+1
            i_posterior=i_posterior+1
    return repeticoes