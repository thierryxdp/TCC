def hashtag(s):
    '''retorna a str s com a presenca do caractere # no inicio, meio e final da str
    str -> str'''
    metade1=s[:len(s)//2]
    metade2=s[len(s)//2:]
    return '#'+metade1+'#'+metade2+'#'