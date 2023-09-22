import math
def hashtag(s):
    '''retorna a string s porém com hashtags no começo, no meio e no final da nova string;
    str -> str'''
    i=math.floor(len(s)/2)
    if len(s)%2==0:
        comeco=s[0:i]
        fim=s[i:]
    else:
        comeco=s[0:i]
        fim=s[i:]
    return '#' + comeco + '#' + final + '#'