def hashtag(s):
    '''adiciona o caractere # a uma strin no 
    seu inicio,meio e final;
    str -> str'''
    return '#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'