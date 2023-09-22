def lingua_p(frase):
    '''Funcao que recebe uma palavra e retorna a mesma traduzida para a lingua do p; isso significa inserir apos cada vogal a letra p e a sequencia de p mais a vogal'''
    '''str -> str'''
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