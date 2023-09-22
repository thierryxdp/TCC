# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x=len(s)//2
    str1=s[0:x]
    str2=s[x:]
    return '#'+str1+'#'+str2+'#'