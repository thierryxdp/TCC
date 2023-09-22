# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    Prparte=len(s)//2
    return ('#'+s[:Prparte]+'#'+s[Prparte:]+'#')