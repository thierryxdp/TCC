def hashtag(s):
    '''Dada uma string, retorna a mesma string com o caractere "#" no seu começo, meio e final.
    str, str -> str'''
    metade = int(len(s)/2)
    return '#' + s[:metade] + '#' + s[metade:] + '#'