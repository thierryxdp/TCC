def hashtag(s):
    '''
       a funcao vai adicionar o simbolo # no inicio, no meio
       e no final da string
       str -> str
    '''
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]'#'