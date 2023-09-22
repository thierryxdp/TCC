# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' Função que coloca # no começo meio e fim da frase; str->str'''
    return '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'