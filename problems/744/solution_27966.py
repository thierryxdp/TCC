'''Retorna uma string e insere # no inicio meio e final
str -> str'''
def hashtag(s):
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s