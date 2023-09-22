"""Uma função que recebe uma string e insere "#" no inicio, no meio e no final. 
Assinatura: str-> str
Testes:
hashtag('123456') =='#123#456#'
hashtag('12345') == '#12#345#'
"""
def hashtag(s):
    meio= len(s)//2
    return '#' + s[ :meio] + '#'+ s[meio: ] + '#'