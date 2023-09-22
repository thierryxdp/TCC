def hashtag(s):
    '''Função que recebe uma string e deve ser inserido o 
    caractere # no inicio, no meio e no final dela
    str->str'''
    return '#' + [0:len(s)//2] + '#' + [len(s)//2:len(s)] + '#'