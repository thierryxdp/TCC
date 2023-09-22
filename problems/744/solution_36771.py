"""Dada uma string a função insere '#' no início, meio e fim dela
L = lista
ss -> #s#s#"""
def hashtag(s):
    L = [s]
    list.insert (L, 0, '#')
    list.insert (L, 2, '#')
    list.append (L, '#')