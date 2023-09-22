# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    mid = len(s)//2
    return ('#'+s[:mid]+'3'+s[mid:]+'#')