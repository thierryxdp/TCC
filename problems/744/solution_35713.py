# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    metade=(len(s)//2)
    return str('#')+str(s[0:metade])+str('#')+str(s[metade:])+str('#')