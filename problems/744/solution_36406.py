def hashtag(s):
    '''Função que recebe uma string s e insere o caractere
    # no inicio, no meio e no final dela.
    str-> str
    '''
    meio = len(s)//2
    return '#' + s[:meio] + '#' + s[meio:] + '#'