def repetidos(numeros):
    '''função que retorna a quantidade de vezes que um numero
    dentro da lista parece consecutivamente
    lista-> int'''
    i_inic=0
    i_post=1
    repeticoes=0
    while i_post<len(numeros):
        if numeros[i_inic]==numeros[i_post]:
            repeticoes=repeticoes+1
            i_inic=i_inic+1
            i_post=i_post+1
        elif numeros[i_post]!=numeros[i_inic]:
            i_inic=i_inic+1
            i_post=i_post+1
    return repeticoes