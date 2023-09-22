def lingua_p(palavra):
    '''uma função que transforma qualquer palavra em uma palavra na lingua do P.
    str -> str'''
    resposta = ''
    letra = ''
    palavra = str.lower(palavra)
    for pal in len(range(palavra)):
        if pal in 'aeiou':
            letra = pal+'p'+pal
            resposta +=letra
    return resposta