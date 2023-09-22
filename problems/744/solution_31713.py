# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    s=s
    new_s='#'+s[:(len(s)//2)]+'#'+s[(len(s)//2):]+'#'
    return new_s