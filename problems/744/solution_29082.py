def hashtag(s):
    '''insere o caractere # no início, no meio e no fim de
    uma string; str -> str'''
    return '#'+s[:(len(s)//2)]+'#'+s[len(s)//2:]+'#'