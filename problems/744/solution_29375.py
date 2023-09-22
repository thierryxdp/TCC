def hashtag(s):
    '''recebe uma sthing e insere o caractere "#" no inicio'''
    '''str->str'''
    meio = len(s)//2
    return '#' + str (s[0:meio]) + '#' + str (s[0:meio]) + '#'