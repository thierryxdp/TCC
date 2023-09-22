# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que retorna string com "#" no ínicio, meio e fim
    str --> str'''
    nova_palavra = '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'
    return nova_palavra