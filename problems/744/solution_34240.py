# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    comp = len(s) // 2 
    nova_palavra = '#' + s[:comp] + '#' + s[comp + 1:] + '#'
    return comp