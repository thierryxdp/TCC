def hashtag(s):
    ''' Função chamada hashtag que recebe uma string
        e insira o caractere ”#” no início, no meio
        e no final dela.
        : param s: str
        : return: str
    '''
    has = '#'+ s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'
    return has