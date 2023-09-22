#Questao 3
def hashtag(s):
    '''
Funcao que recebe uma string "#" no início, no meio e no final dela.
str-> str
    '''
    return "#" + s[: len(s)//2]+ "#" + s[len(s)//2:] + "#"