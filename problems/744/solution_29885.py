from math import*
def hashtag(s):
    """função que recebe uma string e insere um caractere; str-->str"""
    s=("ab")
    metade=len(s)//2
    sub= "#" + s[0:metade] + "#" + s[metade:] + "#"
    return(sub)