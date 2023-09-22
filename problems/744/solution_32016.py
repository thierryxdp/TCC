def hashtag(s:str)->str:
    '''retorna a string com um # no início, meio e fim'''
    n=len(s)
    return ('#'+ s[0:n//2]+'#'+s[(n//2):]+'#')