# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    #hashtag = s[:len(s) //2] + s + s[-(len(s) //2+1):1]
    hashtag = s[:len(s) //2] + s + s[len(s) //2:]
    return hashtag