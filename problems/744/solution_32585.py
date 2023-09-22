def hashtag(s):
    """ A função retorna um string com o caractere
    '#' no início, no meio e no fim """
    
    stringf = '#' + s[0:len(s)//2] + '#' + s[len(s)//2:len(s)]
    
    return stringf