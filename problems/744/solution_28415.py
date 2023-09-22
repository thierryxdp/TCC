# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    a=len(s)
    b=a/2
    c=round(b)
    return "#" + s[0:int(c)] + "#" + s[int(c):] +"#"