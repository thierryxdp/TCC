def hashtag(s):
    '''
    funcao que usa str + # para retornar # entre
    as palavras/letras
    str->str
    '''
    s='#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'
    return s