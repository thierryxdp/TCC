def hashtag(s):
    '''retorna o caractere de hashtag no inicio, no meio
    e no final de uma string'''
    '''str -> str'''
    s = '#' + s + '#'
    meio = len(s)//2
    s = s [:meio] + '#' + s [:meio]
    return s