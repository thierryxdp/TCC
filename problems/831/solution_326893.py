def lingua_p(frase):
    '''Funçao que recebe um parametrocomo de uma palavra( em português) e retorna essa mesma 
    palavra traduzida para a lingua do P.'''
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