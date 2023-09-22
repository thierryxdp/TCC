def hashtag(s):
    '''retorna o caractere de hashtag no inicio, no meio
    e no final de uma string'''
    '''str -> str'''
    string = '#' + s + '#'
    meio = len(string)//2
    string = string [:meio] + '#' + string [:meio]
    return string