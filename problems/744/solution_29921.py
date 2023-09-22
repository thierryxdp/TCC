import math
def par(n):
    return n % 2 == 0

def impar(n):
    return not par(n)
def hashtag(s):
    """Retorna um string na qual o caractere "#" aparece no começo,
    meio e final dela
    str -> str
    
    Casos de teste:
    hashtag('barbearia') = '#barb#earia#'
    hashtag('olhos') ='#ol#hos#'
    hashtag('carvalho') = '#carv#alho#'
    """
    x = len(s) - math.ceil(len(s)/2)
    y = x - 1
    if par(x):
        return '#' + s[0 : x] + '#' + s[x:] + '#'
    if impar(x):
        return '#' + s[0 : x] + '#' + s[x:] + '#'