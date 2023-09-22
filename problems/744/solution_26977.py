def hashtag(s):
    '''função que rebeca uma string e insira o caractere '#' no inicio, no meio e no final dela.'''
    # str-> str
    a = len(s)//2 
    return '#'+ s[:a] + '#' + s[a:] + '#'