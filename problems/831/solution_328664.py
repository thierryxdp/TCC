def lingua_p(palavra: str) -> str:
    '''Traduz palavra para lingua do p'''
    palavra = str.lower(palavra)
    i = 0
    palavrap = ''
    while i < len(palavra):
        if (palavra[i] in 'aeiou'):
            palavrap = palavra[: (i+1)] + 'p' + palavra[i :]
            i += 1
    return palavrap