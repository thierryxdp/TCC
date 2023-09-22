# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função qu recebe uma string e coloca # no inicio, meio e final da string. str -> str'''
    divisao = len(s)//2
    return '#' + s[:divisao] + '#' + s[divisao:] + '#'