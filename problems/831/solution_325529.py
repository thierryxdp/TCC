def lingua_p(palavra):
    '''uma função que transforma qualquer palavra em uma palavra na lingua do P.
    str -> str'''
    resposta = ''
    letra = ''
    palavra = str.lower(palavra)
    for pal in palavra:
        if pal in 'aeiouáéíóú':
            letra = pal+'p'
            resposta +=letra
        resposta += pal    
    return resposta