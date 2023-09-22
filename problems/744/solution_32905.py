'''Funcao que recebe uma string e coloca o caracterw
# no inicio, no meio e no final dela
string->string'''
def hashtag(s):
    meio = len(s)//2
    return '#' + s[0:meio] + '#' + s[meio:] + '#'