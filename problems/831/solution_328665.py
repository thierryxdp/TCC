def lingua_p(palavra: str) -> str:
    '''Traduz palavra para lingua do p'''
    palavra = str.lower(palavra)
    palavrap = ''
    for i in range(len(palavra)):
        if (palavra[i] in 'aeiou'):
            palavrap = palavra[: (i+1)] + 'p' + palavra[i :]
    return palavrap