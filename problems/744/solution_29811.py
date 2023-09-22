# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return str ("#")+(len(s)[0:s//2])+("#")+(len(s)[s//2])+("#")