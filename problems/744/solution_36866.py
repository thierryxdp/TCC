# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x= "#" +s[:int(len(s)/2)] + "#" + s[int(len(s)/2):]+"#"
    return x