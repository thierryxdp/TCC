def lingua_p(palavra: str) -> str:
    '''Traduz palavra para lingua do p'''
    palavrap = ''
    for letra in palavra:
        if str.lower(letra) in 'aeiou':
            palavra = palavra[: (str.index(letra) + 1)] + 'p' + palavra[(str.index(letra):]
    palavrap = palavra
    return palavrap