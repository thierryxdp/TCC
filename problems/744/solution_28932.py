def hashtag(s):
    '''dada uma string (s), retorna o caractere # no inicio, no meio e no final dela
       : str -> str
    '''
    s = '#' + s[0:(len(s)//2)] + '#' + s[(len(s)//2):] + '#'
    return s