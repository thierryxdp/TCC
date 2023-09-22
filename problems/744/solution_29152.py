# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x=len(s)
    # essa função taca 3 hashtags na string
    return str('#') + s[0:round(x/2)] + str('#')+s[round(x/2)+1:]+str('#')