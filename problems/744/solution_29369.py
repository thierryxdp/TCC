def hashtag(s):
    '''insere o caractere '#' no inicio, meio e final da string'''
    '''str -> str'''
metade = len(s)//2
    return '#' + str (s[0:metade]) + '#' + str (s[meio:] + '#'