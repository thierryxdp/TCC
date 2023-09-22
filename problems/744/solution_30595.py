def hashtag(s):
    """
    Em uma string 's', insere '#' no meio da string, antes da primeira e depois da última letra.

    Em caso de uma string com número impar de caractéres, retornará '#' antes do caractére central.

    str -> str
    """

    if len(s) % 2 != 0:
        m = int(len(s)/2 - 0.5)
    else:
        m = int(len(s)/2)

    sN = '#' + s[0:m] + '#' + s[m:len(s)] + '#'
    return sN

    #Casos testes: hashtag('oi') -> '#o#i#'
    #Casos testes: hashtag('Começar') -> '#Com#eçar#'
    #Casos testes: hashtag('FaleiVelho') -> '#Falei#Velho#'