def freq_palavras (strin, letra):
    '''conta quantas vezes a palavra aparece'''
    contador=0
    for item in string:
        if item == letra:
            contador +=1
    return contador