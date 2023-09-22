def hashtag(s):
    '''Recebe uma string e insere o caractere ”#” no início, no meio e no final dela
str -> str'''
    corte1=s[:((len(s))//2)]
    corte2=s[((len(s))//2):]
    return '#'+corte1+'#'+corte2+'#'