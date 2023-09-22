# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    media = len(s) //2
    s="#"+s[0:media]+"#"+s[media:]+"#"
    return s