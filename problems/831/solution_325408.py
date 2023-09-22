def lingua_p(frase):
    '''Essa função recebe uma palavra em portugues e retorna a mesma traduzida para lingua do P
    str -> str'''
    vogais = 'ãaáàeéèiíoóuú'
    vogaisup = str.upper(vogais)
    palavra = ''

    for letra in frase:
        if letra in vogais:
            palavra = palavra +  letra + 'p' + letra
            
        elif letra in vogaisup:
            palavra = palavra +  letra + 'p' + letra
            
        else:
            palavra = palavra + letra
    return str.lower(palavra)