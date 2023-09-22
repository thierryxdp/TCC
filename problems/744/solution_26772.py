from math import*
def hashtag(s):
    """Coloca uma hastag no inicio no meio e no fim de uma string"""
    return str('#'+s[0:floor(int(len(s)/2))]+'#'+s[ceil(int(len(s)/2)):int(len(s))]+'#')