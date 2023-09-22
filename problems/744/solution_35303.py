def hashtag(s):
    '''funcao que recebe uma string e insera o caractere "#" no inicio, no meio e no final dela
    str->str'''
    return '#' + s[:(len(s)//2)] + '#' + s[(len(s)//2):]