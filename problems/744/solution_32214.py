def hashtag(s):
    ''' Esta função insere o caractere '#' no início, no
meio e no fim de uma string s.
str-> str'''
    meio = (len(s)//2)
    return '#' + s[0:meio] + '#' + s[meio:] + '#'