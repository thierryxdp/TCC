def hashtag(s):
    '''funcao que insere uma hashtag (#) no inicio, meio e fim da frase
    str s; str-> str'''
    import math
    x=(math.floor(len(s)/2))
    subs1=s[0:x]
    subs2=s[x:]
    return '#'+str(subs1)+'#'+str(subs2)+'#'