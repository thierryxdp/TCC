# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    n= len(s)
    ind = (n//2)-1
    return "#"+str(s[0:ind])+"#"+str(s[ind:])