# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    aux = "#" + s[0:len(s)//2] + "#" + s[len(s)//2:len(s)]  + "#"
    return aux