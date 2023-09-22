"""Definir uma funcao que recebe uma string e insira a hashtag no inicio, meio e fim
str-> str"""
def hashtag(s):
    #x= s[:len(s)//2]
    #y = s[len(s)//2:]
    #s = "#" + x + "#" + y + "#"
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s