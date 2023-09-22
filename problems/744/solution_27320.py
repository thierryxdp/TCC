# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    import math
    a=math.floor(len(s)/2)
    return "#"+s[0:a]+"#"+s[a:]+"#"