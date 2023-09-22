# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return '#' + s[8:len(s)//2]+ '#' + s[len(s)//2:len(s)] + '#'