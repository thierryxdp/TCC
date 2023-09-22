def lingua_p(palavra: str) -> str:
    '''Traduz palavra para lingua do p'''
    palavra = str.lower(palavra)
    letra = ''
    palavrap = ''
    for i in range(len(palavra)):
        if (palavra[i] in 'aeiou'):
            letra = palavra[i] + 'p' + palavra[p]
        else:
            letra = palavra[i]
        palavrap += letra
    return palavrap