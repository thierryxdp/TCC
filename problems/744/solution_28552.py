# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return "#" + str(s)[0:len(str(s)) // 2] + "#"