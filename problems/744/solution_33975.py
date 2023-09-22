# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que recebe uma string e retorna ela separada com hastags entre algumas letras;
    str -> str'''
    return '#' + s[0:2] + '#' + s[2:] + '#'