def hashtag(s):
    '''retorna o caractere de hashtag no inicio, no meio
    e no final de uma string'''
    '''str -> str'''
    s = '#' + string + '#'
    meio = len(string)//2
    s = string [:meio] + '#' + string [:meio]
    return s