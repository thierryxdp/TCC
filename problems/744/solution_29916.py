import math
def par(n):
    return n % 2 == 0

def impar(n):
    return not par(n)
def hashtag(s):
    x = len(s) - math.ceil(len(s)/2)
    y = x - 1
    if par(x):
        return '#' + s[0 : x] + '#' + s[x:] + '#'
    if impar(x):
        return '#' + s[0 : y] + '#' + s[x:] + '#'