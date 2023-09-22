def hashtag(s):
    '''Função que recebe uma string e deve ser inserido o 
    caractere # no inicio, no meio e no final dela
    str->str'''
    completo = len(s)
    metade = completo//2
    metade1 = s[0:metade]
    metade2 = s[metade:len(s)]
    return '#' + metade1 + '#' + metade2 + '#'