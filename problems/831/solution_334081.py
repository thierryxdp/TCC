def lingua_p(frase):
    '''função que recebe uma palavra como parâmetro e retorna a mesma traduzida para a lingua do p; isso significa inserir após cada vogal a letra p e a sequecia de p mais a vogal. str -> str'''
    vogais = '^^aáàeéèiíoóuú'
    vogaisup = str.upper(vogais)
    palavra = ' '
    for letra in frase:
        if letra in vogais:
            palavra = palavra + letra + 'p' + letra
        elif letra invogaisup:
            palavra = palavra + letra + 'p' + letra 
        else:
            palavra = palavra + letra
    returnstr.lower(palavra)