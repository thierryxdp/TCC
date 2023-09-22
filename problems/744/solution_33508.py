# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x= len(s)//2
    s = '#' + s[0:x] + '#' + s[x+1:] + '#'
    return s