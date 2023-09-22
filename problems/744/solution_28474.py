import math
def hashtag(s):
    """recebe uma string e retorna essa mesma str com # no inicio meio e fim"""
    if len(s)%2!=0:
        p=math.ceil(len(s)/2)
        return '#'+s[0:p-1]+'#'+s[p-1:len(s)+1]+'#'
    elif len(s)%2==0:
        return '#'+s[0:int(len(s)/2)]+'#'+s[int(len(s)/2):len(s)+1]+'#'