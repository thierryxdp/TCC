def hashtag(s):
    '''recebe uma string e insere um caractere de # no meio, no inicio e no final dela'''
    '''str-> str'''
    return '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'