def hashtag (x):
    '''insere o caractere # no início, no meio e no final de uma str x; str->str'''
    a=len(x)//2
    return '#'+x[0:a]+'#'+x[a:]