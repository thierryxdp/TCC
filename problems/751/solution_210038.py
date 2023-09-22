def conta_palavra(frase):

    '''Conta o número de palavras em uma frase '''

    # str -> int

    palavras = frase.count(' ')
    palavras = palavras + 1
    
    if frase[0] == ' ':

        palavras = palavras - 1

    elif frase[0] and frase[-1:] == ' ':

        palavras = palvras - 2

    elif frase [-1:] == ' ':

        palavras = palavras - 1

    return palavras