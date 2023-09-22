# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)==4:
        return('#'+s[0:2]+'#'+s[2:]+'#')
    if len(s)==5:
        return('#'+s[0:2]+'#'+s[2:]+'#')
    if len(s)==1:
        return('#'+s[::]+'#')
    if len(s)==6:
        return('#'+s[0:4]+'#'+s[4:])
    if len(s)==7:
        return ('#'+s[0,4]+'#'+s[4:])
    if len(s)==8:
        return('#'+s[0,5]+'#'+s[5:]+'#')