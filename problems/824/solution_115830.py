def uppCons(frase):
    '''retorna a frase de entrada com todas as consoantes em maíusculae os demais caractéres como estavam; str -> str'''

    i = 0
    resultado = ''

    while i<len(frase):
        if frase[i] in 'çbcdfghjklmnpqrstvxywzÇBCDFGHJKLMNPQRSTVXYWZ':
            resultado = resultado + str.upper(frase[i])
        else:
            resultado = resultado + frase[i]
        i = i + 1

    return resultado