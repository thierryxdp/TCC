"""Definir uma funcao que recebe uma string e insira a hashtag no inicio, meio e fim
str-> str"""
def hashtag(S):
    #x= S[:len(S)//2]
    #y = S[len(S)//2:]
    #S = "#" + x + "#" + y + "#"
    S = "#" + S[:len(S)//2] + "#" + S[len(S)//2:] + "#"
    return S