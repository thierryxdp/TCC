# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    middle = s/2
    hashtag = "#" + s[:middle] + "#" + s[middle:] + "#"
    return hashtag