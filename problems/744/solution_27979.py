def hashtag(s):
    '''Funcao que retorna uma string com o caractere # no inicio, meio e 
    fim dela
    str-> str'''
    metade = len(s)//2
    return '#' + s[:metade] + '#' + s[metade:] + '#'